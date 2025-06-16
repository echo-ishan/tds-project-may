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
TEST_JSON_FILE = "test_thread.json" # The file you create from paste.txt
OUTPUT_MD_FILE = "test_output.md"
DISCOURSE_BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
IGNORE_IMAGE_PATTERNS = ["/user_avatar/", "https://emoji.discourse-cdn.com/", "/images/transparent.png", "https://avatars.discourse-cdn.com/"]

# --- Initialize Google Gemini Client ---
try:
    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    if not gemini_api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    genai.configure(api_key=gemini_api_key)
    GEMINI_MODEL = genai.GenerativeModel('gemini-1.5-flash-latest')
    print("✓ Gemini client initialized successfully.")
except Exception as e:
    GEMINI_MODEL = None
    print(f"[!] Error: Gemini client could not be initialized. {e}")

# --- Helper Functions (with the crucial fix) ---
def get_image_description_gemini(image_url):
    if not GEMINI_MODEL:
        return "[Image description skipped: Gemini client not initialized]"
    print(f"  > Analyzing image with Gemini: {image_url}")
    try:
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        mime_type = Image.MIME.get(img.format)
        if not mime_type: return "[Image description failed: Unknown image format]"

        image_part = {"mime_type": mime_type, "data": response.content}
        prompt = "You are an expert at analyzing screenshots from a data science course forum. Describe the key information. Transcribe any code, commands, or error messages exactly as they appear."
        api_response = GEMINI_MODEL.generate_content([prompt, image_part])
        
        if not hasattr(api_response, 'text') or not api_response.text:
            print("    [!] Warning: Gemini API returned an empty text response.")
            return "[Image analysis resulted in empty text]"
        return api_response.text.strip()
    except Exception as e:
        print(f"    [!] Error analyzing image with Gemini: {e}")
        return "[Image description failed due to an API or network error]"

def build_full_url(path, base_url):
    if not path or path.startswith("http"): return path
    if path.startswith("//"): return "https:" + path
    if path.startswith("/"): return base_url + path
    return f"{base_url}/{path}"

# (THE FIX - PART 1: This function now correctly returns the descriptions dictionary)
def preprocess_and_enrich_html(html_content, base_url):
    if not html_content: return "", {}
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
            # Store the final formatted markdown in the dictionary
            image_descriptions[placeholder] = f"\n\n> **Image Content:** *{description_text}*\n\n"
            node_to_replace.replace_with(placeholder)
            
            time.sleep(1) # Be respectful to the API
        except Exception as e:
            print(f"    [!] Skipped processing an image tag due to an unexpected error: {e}")
            if 'node_to_replace' in locals() and not node_to_replace.is_root:
                 node_to_replace.decompose()
            continue

    for a_tag in soup.find_all('a'):
        if a_tag.has_attr('href'):
            a_tag['href'] = build_full_url(a_tag['href'], base_url)
            
    return str(soup), image_descriptions

# --- The Function Under Test (with the crucial fix) ---
def convert_thread(json_path, md_path):
    """Reads a single JSON file and converts it to enriched Markdown."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f: 
            data = json.load(f)
    except Exception as e:
        print(f"[!] Error reading {json_path}: {e}")
        return

    posts = data.get('post_stream', {}).get('posts', [])
    if not posts: return
    
    markdown_output = [f"# Topic: {data.get('title', 'Discourse Thread')}\n"]
    for post in posts:
        if post.get('action_code') or not post.get('cooked', '').strip():
            continue

        author = post.get('display_username', 'Unknown')
        user_title, flair_name = post.get('user_title'), post.get('flair_name')
        author_role = f" ({', '.join(filter(None, [user_title, flair_name]))})" if user_title or flair_name else ""
        
        created_dt = datetime.fromisoformat(post['created_at'].replace('Z', ''))
        date_str = created_dt.strftime('%B %d, %Y, %H:%M UTC')
        
        processed_html, image_descriptions = preprocess_and_enrich_html(post['cooked'], DISCOURSE_BASE_URL)
        markdown_content = md(processed_html, heading_style="ATX").strip()
        
        # THE FIX: Replace escaped placeholders instead of original ones
        for placeholder, description in image_descriptions.items():
            escaped_placeholder = placeholder.replace("_", "\\_")
            print(f"Looking for: {escaped_placeholder}")
            if escaped_placeholder in markdown_content:
                print(f"Found and replacing!")
                markdown_content = markdown_content.replace(escaped_placeholder, description)
            else:
                print(f"Not found in markdown")

        if markdown_content:
            markdown_output.append(f"### Post #{post.get('post_number')} by **{author}**{author_role}")
            markdown_output.append(f"*{date_str}*")
            markdown_output.append(markdown_content)

        reactions = post.get('reactions', [])
        if reactions:
            emoji_map = {'heart': '❤️', '+1': '👍'}
            reaction_strs = [f"{emoji_map.get(r['id'], r['id'])} {r['count']}" for r in reactions]
            markdown_output.append(f"\n**Reactions:** {' '.join(reaction_strs)}")

        markdown_output.append("\n---\n")

    with open(md_path, 'w', encoding='utf-8') as f: 
        f.write("\n".join(markdown_output))
    print(f"✓ Converted {os.path.basename(json_path)}")


def run_integration_test():
    """Orchestrates the test for the convert_thread function."""
    if not GEMINI_MODEL:
        print("[!] Aborting test: Gemini client is not available.")
        return
        
    if not os.path.exists(TEST_JSON_FILE):
        print(f"[!] Aborting test: Input file '{TEST_JSON_FILE}' not found.")
        print(f"Please save the content from the provided paste.txt file as {TEST_JSON_FILE} in this directory.")
        return

    print(f"--- Running Integration Test on convert_thread ---")
    convert_thread(TEST_JSON_FILE, OUTPUT_MD_FILE)
    print("--------------------------------------------------")

if __name__ == "__main__":
    run_integration_test()
