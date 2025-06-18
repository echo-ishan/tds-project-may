import os
import json
import time
import re
import numpy as np
import requests
from tqdm import tqdm
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
DISCOURSE_DIR = "discourse_md"
TDS_PAGES_DIR = "tds_pages_md"
OUTPUT_FILE = "knowledge_embedding1.npz"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
API_TOKEN = os.getenv("OPENAI_API_KEY")
AIPROXY_EMBEDDINGS_URL = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"

def extract_discourse_urls(content):
    """Extract topic and post URLs from discourse markdown files."""
    urls = {}
    
    # Extract topic URL
    topic_url_match = re.search(r'\*\*Topic URL:\*\*\s*\[Link\]\(([^)]+)\)', content)
    if topic_url_match:
        urls['topic_url'] = topic_url_match.group(1)
    
    # Extract all post URLs
    post_url_matches = re.findall(r'\*\*Post URL:\*\*\s*\[Link\]\(([^)]+)\)', content)
    urls['post_urls'] = post_url_matches
    
    return urls

def extract_tds_frontmatter(content):
    """Extract frontmatter metadata from TDS course files."""
    frontmatter = {}
    
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.search(frontmatter_pattern, content, re.DOTALL)
    
    if match:
        frontmatter_text = match.group(1)
        for line in frontmatter_text.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip('"')
    
    return frontmatter

def create_intelligent_chunks(text, source_type, metadata, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """Create chunks with source-specific intelligence."""
    if not text or len(text) <= chunk_size:
        return [text] if text else []
    
    chunks = []
    
    if source_type == "discourse":
        # For discourse posts, split by post boundaries first
        post_sections = re.split(r'\n---\n', text)
        
        for section in post_sections:
            if len(section) <= chunk_size:
                chunks.append(section)
            else:
                # Split large posts into smaller chunks
                section_chunks = split_by_paragraphs(section, chunk_size, chunk_overlap)
                chunks.extend(section_chunks)
    
    elif source_type == "tds":
        # For TDS content, respect markdown structure
        chunks = create_markdown_aware_chunks(text, chunk_size, chunk_overlap)
    
    return chunks

def split_by_paragraphs(text, chunk_size, chunk_overlap):
    """Split text by paragraphs with intelligent overlap."""
    paragraphs = re.split(r'\n\s*\n', text)
    chunks = []
    current_chunk = []
    current_size = 0
    
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        
        para_size = len(paragraph)
        
        if current_size + para_size > chunk_size and current_chunk:
            # Save current chunk
            chunks.append('\n\n'.join(current_chunk))
            
            # Create overlap
            if chunk_overlap > 0 and current_chunk:
                overlap_text = '\n\n'.join(current_chunk[-1:])
                if len(overlap_text) > chunk_overlap:
                    overlap_text = overlap_text[-chunk_overlap:]
                current_chunk = [overlap_text]
                current_size = len(overlap_text)
            else:
                current_chunk = []
                current_size = 0
        
        current_chunk.append(paragraph)
        current_size += para_size + 2
    
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks

def create_markdown_aware_chunks(text, chunk_size, chunk_overlap):
    """Enhanced markdown chunking that preserves structure."""
    if len(text) <= chunk_size:
        return [text]
    
    # Split by headers first
    header_sections = re.split(r'\n(?=#{1,6}\s)', text)
    chunks = []
    current_chunk = ""
    
    for section in header_sections:
        if len(current_chunk) + len(section) <= chunk_size:
            current_chunk += "\n" + section if current_chunk else section
        else:
            if current_chunk:
                chunks.append(current_chunk)
            
            if len(section) <= chunk_size:
                current_chunk = section
            else:
                # Split large sections
                section_chunks = split_by_paragraphs(section, chunk_size, chunk_overlap)
                chunks.extend(section_chunks[:-1])
                current_chunk = section_chunks[-1] if section_chunks else ""
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def process_discourse_files(discourse_dir):
    """Process discourse markdown files with URL extraction."""
    if not os.path.exists(discourse_dir):
        print(f"Warning: Directory '{discourse_dir}' not found.")
        return [], []
    
    all_chunks = []
    all_metadata = []
    
    for file_name in tqdm(os.listdir(discourse_dir), desc="Processing Discourse Files"):
        if not file_name.endswith('.md'):
            continue
        
        file_path = os.path.join(discourse_dir, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        
        # Extract URLs from discourse content
        urls = extract_discourse_urls(content)
        
        # Create chunks
        chunks = create_intelligent_chunks(content, "discourse", urls)
        
        for i, chunk in enumerate(chunks):
            # Add URL context to chunk
            if urls.get('topic_url'):
                enhanced_chunk = f"Discussion Topic: {urls['topic_url']}\n\n{chunk}"
            else:
                enhanced_chunk = chunk
            
            all_chunks.append(enhanced_chunk)
            all_metadata.append({
                'source_type': 'discourse',
                'source_dir': discourse_dir,
                'file_name': file_name,
                'chunk_index': i,
                'total_chunks': len(chunks),
                'topic_url': urls.get('topic_url'),
                'post_urls': urls.get('post_urls', []),
                'has_urls': bool(urls.get('topic_url') or urls.get('post_urls'))
            })
    
    return all_chunks, all_metadata

def process_tds_files(tds_dir):
    """Process TDS course files with frontmatter extraction."""
    if not os.path.exists(tds_dir):
        print(f"Warning: Directory '{tds_dir}' not found.")
        return [], []
    
    all_chunks = []
    all_metadata = []
    
    for file_name in tqdm(os.listdir(tds_dir), desc="Processing TDS Files"):
        if not file_name.endswith('.md'):
            continue
        
        file_path = os.path.join(tds_dir, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        
        # Extract frontmatter
        frontmatter = extract_tds_frontmatter(content)
        
        # Remove frontmatter from content for chunking
        content_without_frontmatter = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
        
        # Create chunks
        chunks = create_intelligent_chunks(content_without_frontmatter, "tds", frontmatter)
        
        for i, chunk in enumerate(chunks):
            # Add course URL context
            if frontmatter.get('original_url'):
                enhanced_chunk = f"Course Section: {frontmatter['original_url']}\nTitle: {frontmatter.get('title', 'Unknown')}\n\n{chunk}"
            else:
                enhanced_chunk = chunk
            
            all_chunks.append(enhanced_chunk)
            all_metadata.append({
                'source_type': 'tds_course',
                'source_dir': tds_dir,
                'file_name': file_name,
                'chunk_index': i,
                'total_chunks': len(chunks),
                'original_url': frontmatter.get('original_url'),
                'title': frontmatter.get('title'),
                'downloaded_at': frontmatter.get('downloaded_at'),
                'has_url': bool(frontmatter.get('original_url'))
            })
    
    return all_chunks, all_metadata

def generate_embeddings(chunks, api_token, batch_size=15):
    """Generate embeddings using text-embedding-3-small."""
    if not api_token:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return None
    
    all_embeddings = []
    failed_batches = []
    
    for i in tqdm(range(0, len(chunks), batch_size), desc="Generating Embeddings"):
        batch = chunks[i:i + batch_size]
        
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "text-embedding-3-small",
            "input": batch
        }
        
        try:
            response = requests.post(AIPROXY_EMBEDDINGS_URL, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                batch_embeddings = [item['embedding'] for item in result['data']]
                all_embeddings.extend(batch_embeddings)
            else:
                print(f"\nAPI Error on batch {i//batch_size + 1}: {response.status_code}")
                failed_batches.append(i//batch_size + 1)
                # Add zero embeddings as placeholders
                embedding_dim = 1536
                all_embeddings.extend(np.zeros((len(batch), embedding_dim), dtype=np.float32).tolist())
        
        except Exception as e:
            print(f"\nError on batch {i//batch_size + 1}: {e}")
            failed_batches.append(i//batch_size + 1)
            embedding_dim = 1536
            all_embeddings.extend(np.zeros((len(batch), embedding_dim), dtype=np.float32).tolist())
        
        time.sleep(1)  # Rate limiting
    
    if failed_batches:
        print(f"\nWarning: {len(failed_batches)} batches failed")
    
    return all_embeddings

def save_embeddings_with_stats(embeddings, chunks, metadata, output_file):
    """Save embeddings with comprehensive statistics."""
    if not embeddings:
        print("No embeddings generated. Exiting.")
        return
    
    embeddings_array = np.array(embeddings, dtype=np.float32)
    chunks_array = np.array(chunks, dtype=object)
    metadata_json = json.dumps(metadata, indent=2)
    
    # Calculate statistics
    discourse_count = sum(1 for m in metadata if m['source_type'] == 'discourse')
    tds_count = sum(1 for m in metadata if m['source_type'] == 'tds_course')
    url_count = sum(1 for m in metadata if m.get('has_url') or m.get('has_urls'))
    
    stats = {
        'total_chunks': len(embeddings),
        'discourse_chunks': discourse_count,
        'tds_course_chunks': tds_count,
        'chunks_with_urls': url_count,
        'embedding_model': 'text-embedding-3-small',
        'embedding_dimension': embeddings_array.shape[1],
        'generation_timestamp': time.time()
    }
    
    np.savez_compressed(
        output_file,
        embeddings=embeddings_array,
        chunks=chunks_array,
        metadata=metadata_json,
        statistics=json.dumps(stats)
    )
    
    print(f"\n✅ Successfully saved {len(embeddings)} embeddings to '{output_file}'")
    print(f"📊 Statistics:")
    print(f"   • Total chunks: {len(embeddings)}")
    print(f"   • Discourse posts: {discourse_count}")
    print(f"   • TDS course content: {tds_count}")
    print(f"   • Chunks with URLs: {url_count}")
    print(f"   • File size: {os.path.getsize(output_file) / 1024**2:.2f} MB")

def main():
    """Main execution function."""
    print("🚀 Starting Enhanced Embeddings Generation")
    print("=" * 50)
    
    # Process both directories
    discourse_chunks, discourse_metadata = process_discourse_files(DISCOURSE_DIR)
    tds_chunks, tds_metadata = process_tds_files(TDS_PAGES_DIR)
    
    # Combine all data
    all_chunks = discourse_chunks + tds_chunks
    all_metadata = discourse_metadata + tds_metadata
    
    if not all_chunks:
        print("❌ No chunks found. Check your directories.")
        return
    
    print(f"\n📈 Processing Summary:")
    print(f"   • Discourse chunks: {len(discourse_chunks)}")
    print(f"   • TDS course chunks: {len(tds_chunks)}")
    print(f"   • Total chunks: {len(all_chunks)}")
    
    # Generate embeddings
    print(f"\n🔮 Generating embeddings with text-embedding-3-small...")
    embeddings = generate_embeddings(all_chunks, API_TOKEN)
    
    if embeddings is None:
        print("❌ Failed to generate embeddings.")
        return
    
    # Save results
    save_embeddings_with_stats(embeddings, all_chunks, all_metadata, OUTPUT_FILE)
    print(f"\n🎉 Embeddings generation complete!")

if __name__ == "__main__":
    main()
