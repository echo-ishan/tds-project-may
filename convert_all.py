import os
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
from io import BytesIO

# --- Configuration ---
load_dotenv()
INPUT_DIR = "discourse_json"
OUTPUT_DIR = "discourse_md"
DISCOURSE_BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"

IGNORE_IMAGE_PATTERNS = [
    "/user_avatar/",
    "https://emoji.discourse-cdn.com/",
    "/images/transparent.png",
    "https://avatars.discourse-cdn.com/"
]

# --- Initialize Google Gemini Client ---
try:
    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    if not gemini_api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    genai.configure(api_key=gemini_api_key)
    GEMINI_MODEL = genai.GenerativeModel('gemini-2.0-flash')
    print("✓ Gemini client initialized successfully.")
except Exception as e:
    GEMINI_MODEL = None
    print(f"[!] Error: Gemini client could not be initialized. {e}")

# --- Helper Functions ---
def get_image_description_gemini(image_url):
    """Generates concise image descriptions using Gemini."""
    if not GEMINI_MODEL:
        return "[Image description skipped]"

    print(f"  > Analyzing image: {image_url}...")
    try:
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        mime_type = Image.MIME.get(img.format)
        if not mime_type:
            return "[Unsupported image format]"

        image_part = {"mime_type": mime_type, "data": response.content}
        prompt = """You are an expert at analyzing screenshots from a data science course forum. Analyze this technical screenshot and provide a concise description (4-5 sentences max) focusing on:
1. Visible code snippets/error messages (transcribe exactly)
2. UI elements relevant to the problem
3. Data visualizations/charts
4. Key textual content related to technical issues
Omit decorative elements, avatars, and UI chrome. Prioritize actionable technical details."""

        api_response = GEMINI_MODEL.generate_content([prompt, image_part])
        return api_response.text.strip()
        
    except Exception as e:
        print(f"    [!] Image analysis failed: {e}")
        return "[Image description unavailable]"

def build_full_url(path, base_url):
    if not path or path.startswith("http"): return path
    if path.startswith("//"): return "https:" + path
    if path.startswith("/"): return base_url + path
    return f"{base_url}/{path}"

def preprocess_and_enrich_html(html_content, base_url):
    if not html_content: return ""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    image_descriptions = {}

    for img_tag in soup.find_all('img'):
        try:
            node_to_replace = img_tag.parent if img_tag.parent.name == 'a' and 'lightbox' in img_tag.parent.get('class', []) else img_tag
            image_url = build_full_url(node_to_replace.get('href') or img_tag.get('src'), base_url)

            if not image_url or not image_url.startswith("http"):
                node_to_replace.decompose()
                continue

            if any(pattern in image_url for pattern in IGNORE_IMAGE_PATTERNS):
                node_to_replace.decompose()
                continue
            
            description_text = get_image_description_gemini(image_url)
            placeholder = f"__IMAGE_PLACEHOLDER_{image_url}__"
            image_descriptions[placeholder] = f"\n\n> **Image:** {description_text}\n\n"
            node_to_replace.replace_with(placeholder)
            
            time.sleep(1)

        except Exception as e:
            print(f"    [!] Image processing error: {e}")
            if 'node_to_replace' in locals() and not node_to_replace.is_root:
                 node_to_replace.decompose()
            continue

    for a_tag in soup.find_all('a'):
        if a_tag.has_attr('href'):
            a_tag['href'] = build_full_url(a_tag['href'], base_url)
            
    return str(soup), image_descriptions

def convert_thread(json_path, md_path):
    """Converts JSON thread to Markdown with enhanced metadata."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f: 
            data = json.load(f)
    except Exception as e:
        print(f"[!] Error reading {json_path}: {e}")
        return

    # Build topic metadata
    posts = data.get('post_stream', {}).get('posts', [])
    if not posts: return
    
    topic_id = data.get('id', '')
    slug = data.get('slug', '')
    topic_url = f"{DISCOURSE_BASE_URL}/t/{slug}/{topic_id}"
    
    markdown_output = [
        f"# {data.get('title', 'Discourse Thread')}",
        f"**Topic URL:** [Link]({topic_url})  ",
        f"**Created:** {datetime.fromisoformat(data['created_at'].replace('Z','')).strftime('%B %d, %Y')}  ",
        f"**Posts:** {len(posts)}  ",
        "\n---\n"
    ]

    for post in posts:
        if post.get('action_code') or not post.get('cooked', '').strip():
            continue

        # Post metadata
        post_number = post.get('post_number')
        post_url = f"{topic_url}/{post_number}"
        author = post.get('display_username', 'Unknown')
        user_title = post.get('user_title')
        flair_name = post.get('flair_name')
        created_dt = datetime.fromisoformat(post['created_at'].replace('Z', ''))
        
        markdown_output.extend([
            f"### Post #{post_number} by **{author}**",
            f"*{created_dt.strftime('%B %d, %Y, %H:%M UTC')}*  ",
            f"**Post URL:** [Link]({post_url})  ",
            f"**Role:** {user_title or ''} {flair_name or ''}".strip()
        ])

        if post.get('reply_to_post_number'):
            reply_to = post.get('reply_to_user', {}).get('username', f"Post #{post['reply_to_post_number']}")
            markdown_output.append(f"> Replying to @{reply_to}")

        # Process content
        processed_html, image_descriptions = preprocess_and_enrich_html(post['cooked'], DISCOURSE_BASE_URL)
        markdown_content = md(processed_html, heading_style="ATX").strip()
        
        for placeholder, description in image_descriptions.items():
            escaped_placeholder = placeholder.replace("_", "\\_")
            markdown_content = markdown_content.replace(escaped_placeholder, description)

        if markdown_content:
            markdown_output.append("\n" + markdown_content)

        # Reactions
        if reactions := post.get('reactions'):
            emoji_map = {'heart': '❤️', '+1': '👍'}
            reaction_strs = [f"{emoji_map.get(r['id'], r['id'])} {r['count']}" for r in reactions]
            markdown_output.append(f"\n**Reactions:** {' '.join(reaction_strs)}")

        markdown_output.append("\n---\n")

    with open(md_path, 'w', encoding='utf-8') as f: 
        f.write("\n".join(markdown_output))
    print(f"✓ Converted {os.path.basename(json_path)}")

def main():
    if not GEMINI_MODEL:
        print("[!] Aborting: Gemini client unavailable.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    json_files = sorted(f for f in os.listdir(INPUT_DIR) if f.endswith('.json'))
    
    if not json_files:
        print(f"[!] No JSON files in {INPUT_DIR}"); return

    print(f"--- Converting {len(json_files)} files ---")
    for filename in json_files:
        json_path = os.path.join(INPUT_DIR, filename)
        md_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}.md")
        convert_thread(json_path, md_path)

    print("\n--- Conversion complete ---")

if __name__ == "__main__":
    main()
