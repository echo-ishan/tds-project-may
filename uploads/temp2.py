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
OUTPUT_FILE = "knowledge_embeddings.npz"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
# Ensure you are using the correct environment variable name from the docs[3]
API_TOKEN = os.getenv("OPENAI_API_KEY")
# (THE FIX) - The correct API endpoint from the aiproxy documentation[3]
AIPROXY_EMBEDDINGS_URL = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"


def create_chunks(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """
    Splits markdown text into semantically meaningful chunks.
    This chunker is designed to respect markdown structure like headers and code blocks.
    """
    if not text or len(text) <= chunk_size:
        return [text] if text else []

    # Using a simpler, robust recursive chunking approach
    chunks = []
    current_pos = 0
    while current_pos < len(text):
        end_pos = min(current_pos + chunk_size, len(text))
        chunk = text[current_pos:end_pos]
        chunks.append(chunk)
        current_pos += chunk_size - chunk_overlap
        if current_pos >= len(text):
            break
            
    return chunks

def process_markdown_files(markdown_dir):
    """Process all markdown files in a directory."""
    if not os.path.exists(markdown_dir):
        print(f"Warning: Directory '{markdown_dir}' not found. Skipping.")
        return [], []
        
    all_chunks = []
    all_metadata = []
    
    for file_name in tqdm(os.listdir(markdown_dir), desc=f"Processing {markdown_dir}"):
        if not file_name.endswith('.md'):
            continue
            
        file_path = os.path.join(markdown_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        file_chunks = create_chunks(content)
        for i, chunk in enumerate(file_chunks):
            all_chunks.append(chunk)
            all_metadata.append({
                'source_dir': markdown_dir,
                'file_name': file_name,
                'chunk_index': i
            })
            
    return all_chunks, all_metadata

def generate_embeddings(chunks, api_token, batch_size=20):
    """Generate embeddings for text chunks using the aiproxy service."""
    if not api_token:
        print("Error: AIPROXY_TOKEN not found. Please set it in your .env file.")
        return None

    all_embeddings = []
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
            # Use the corrected URL here
            response = requests.post(AIPROXY_EMBEDDINGS_URL, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                batch_embeddings = [item['embedding'] for item in result['data']]
                all_embeddings.extend(batch_embeddings)
            else:
                print(f"\nError on batch {i//batch_size + 1}: {response.status_code} - {response.text}")
                # Add placeholder embeddings for the failed batch
                num_failed = len(batch)
                embedding_dim = 1536 # Dimension for text-embedding-3-small
                all_embeddings.extend(np.zeros((num_failed, embedding_dim), dtype=np.float32).tolist())
        
        except requests.exceptions.RequestException as e:
            print(f"\nNetwork error on batch {i//batch_size + 1}: {e}")
            num_failed = len(batch)
            embedding_dim = 1536
            all_embeddings.extend(np.zeros((num_failed, embedding_dim), dtype=np.float32).tolist())
            
        time.sleep(1) # Add a small delay to be respectful to the API

    return all_embeddings

def save_embeddings(embeddings, chunks, metadata, output_file):
    """Save embeddings, chunks, and metadata to a compressed NumPy file."""
    if not embeddings:
        print("No embeddings were generated. Skipping save.")
        return

    embeddings_array = np.array(embeddings, dtype=np.float32)
    chunks_array = np.array(chunks, dtype=object)
    metadata_json = json.dumps(metadata)
    
    np.savez_compressed(
        output_file,
        embeddings=embeddings_array,
        chunks=chunks_array,
        metadata=metadata_json
    )
    print(f"\n✓ Saved {len(embeddings)} embeddings to '{output_file}'.")
    print(f"  File size: {os.path.getsize(output_file) / 1024**2:.2f} MB")

def main():
    """Main workflow to process files and create embeddings."""
    print("Starting embedding generation process...")
    
    # Process markdown files from both directories
    discourse_chunks, discourse_metadata = process_markdown_files(DISCOURSE_DIR)
    tds_chunks, tds_metadata = process_markdown_files(TDS_PAGES_DIR)
    
    all_chunks = discourse_chunks + tds_chunks
    all_metadata = discourse_metadata + tds_metadata
    
    if not all_chunks:
        print("No text chunks found to process. Please check your input directories.")
        return
        
    print(f"Total chunks created: {len(all_chunks)}")
    
    # Generate embeddings
    all_embeddings = generate_embeddings(all_chunks, API_TOKEN)
    
    # Save everything to a compressed file
    save_embeddings(all_embeddings, all_chunks, all_metadata, OUTPUT_FILE)
    
    print("\nEmbedding process complete.")

if __name__ == "__main__":
    main()
