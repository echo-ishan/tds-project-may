import os
import json
import time
import numpy as np
import requests
import re
from tqdm import tqdm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
DISCOURSE_DIR = "discourse_md"
TDS_PAGES_DIR = "tds_pages_md"
OUTPUT_FILE = "knowledge_embeddings.npz"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
API_TOKEN = os.getenv("OPENAI_API_KEY")

# Function to create chunks from text
def create_chunks(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """
    Split markdown text into semantically meaningful chunks while preserving structure.
    
    This chunker is specifically designed for RAG systems working with markdown content.
    It preserves document structure, maintains header context, and ensures semantic
    coherence for optimal retrieval performance.
    
    Args:
        text (str): The markdown text to split
        chunk_size (int): Maximum size of each chunk in characters
        chunk_overlap (int): Overlap between chunks in characters
        
    Returns:
        list: List of text chunks
    """
    # If text is shorter than chunk_size, return it as a single chunk
    if not text or len(text) <= chunk_size:
        return [text] if text else []
    
    # Define patterns for markdown elements
    header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
    code_block_pattern = re.compile(r'(``````)', re.DOTALL)
    list_pattern = re.compile(r'((?:^|\n)(?:\s*[-*+]|\s*\d+\.)\s+.+(?:\n\s+.+)*)+', re.MULTILINE)
    table_pattern = re.compile(r'((?:^|\n)\|.+\|(?:\n\|[-:]+\|)+(?:\n\|.+\|)+)', re.MULTILINE)
    blockquote_pattern = re.compile(r'((?:^|\n)>\s+.+(?:\n>\s+.+)*)', re.MULTILINE)
    
    # Function to extract header hierarchy
    def get_header_hierarchy(text, position):
        """Get all headers that apply at a given position."""
        headers = []
        for match in header_pattern.finditer(text[:position]):
            level = len(match.group(1))
            content = match.group(2).strip()
            
            # Keep only headers of higher levels
            headers = [h for h in headers if h[0] < level]
            headers.append((level, content))
        
        return headers
    
    # Function to format header hierarchy as markdown
    def format_headers(headers):
        """Convert header tuples to markdown text."""
        return "\n".join([('#' * level + ' ' + content) for level, content in headers])
    
    # Find all special elements
    elements = []
    
    # Find headers
    for match in header_pattern.finditer(text):
        elements.append((match.start(), match.end(), 'header', match.group(0)))
    
    # Find code blocks
    for match in code_block_pattern.finditer(text):
        elements.append((match.start(), match.end(), 'code_block', match.group(0)))
    
    # Find lists
    for match in list_pattern.finditer(text):
        elements.append((match.start(), match.end(), 'list', match.group(0)))
    
    # Find tables
    for match in table_pattern.finditer(text):
        elements.append((match.start(), match.end(), 'table', match.group(0)))
    
    # Find blockquotes
    for match in blockquote_pattern.finditer(text):
        elements.append((match.start(), match.end(), 'blockquote', match.group(0)))
    
    # Sort by position
    elements.sort()
    
    # Split text into chunks
    chunks = []
    current_chunk = []
    current_size = 0
    last_position = 0
    
    # Process each special element
    for start, end, element_type, content in elements:
        # If there's text between the last element and this one, process it
        if start > last_position:
            text_between = text[last_position:start].strip()
            if text_between:
                # Split text between elements into paragraphs
                paragraphs = re.split(r'\n\n+', text_between)
                for paragraph in paragraphs:
                    paragraph = paragraph.strip()
                    if not paragraph:
                        continue
                    
                    # If adding this paragraph would exceed chunk_size, start a new chunk
                    if current_size + len(paragraph) + 2 > chunk_size and current_chunk:
                        # Save current chunk
                        chunks.append("\n\n".join(current_chunk))
                        
                        # Start new chunk with header context
                        headers = get_header_hierarchy(text, last_position)
                        if headers:
                            header_text = format_headers(headers)
                            current_chunk = [header_text]
                            current_size = len(header_text)
                        else:
                            current_chunk = []
                            current_size = 0
                    
                    # Add paragraph to current chunk
                    current_chunk.append(paragraph)
                    current_size += len(paragraph) + 2  # +2 for "\n\n"
        
        # Process the special element
        # If it's a header, always include it
        if element_type == 'header':
            # If we have content and this is a major header (h1, h2), start a new chunk
            header_level = len(re.match(r'^(#+)', content).group(1))
            if header_level <= 2 and current_chunk and current_size > 0:
                chunks.append("\n\n".join(current_chunk))
                current_chunk = []
                current_size = 0
            
            # Add header to current chunk
            current_chunk.append(content)
            current_size += len(content) + 2
        else:
            # For other elements, check if they fit in the current chunk
            if current_size + len(content) + 2 > chunk_size:
                # If the element itself is larger than chunk_size, handle it specially
                if len(content) > chunk_size:
                    # First, save the current chunk
                    if current_chunk:
                        chunks.append("\n\n".join(current_chunk))
                    
                    # For code blocks and tables, keep them intact if possible
                    if element_type in ['code_block', 'table']:
                        # Get header context
                        headers = get_header_hierarchy(text, start)
                        if headers:
                            header_text = format_headers(headers)
                            chunks.append(header_text + "\n\n" + content)
                        else:
                            chunks.append(content)
                    else:
                        # For lists and other elements, try to split them
                        if element_type == 'list':
                            # Split list by items
                            list_items = re.findall(r'(?:^|\n)(\s*[-*+]|\s*\d+\.)\s+.+(?:\n\s+.+)*', content)
                            
                            # Get header context
                            headers = get_header_hierarchy(text, start)
                            header_text = format_headers(headers) if headers else ""
                            
                            current_list_chunk = [header_text] if header_text else []
                            current_list_size = len(header_text) + 2 if header_text else 0
                            
                            for item in list_items:
                                if current_list_size + len(item) + 2 > chunk_size and current_list_chunk:
                                    chunks.append("\n\n".join(current_list_chunk))
                                    current_list_chunk = [header_text] if header_text else []
                                    current_list_size = len(header_text) + 2 if header_text else 0
                                
                                current_list_chunk.append(item)
                                current_list_size += len(item) + 2
                            
                            if current_list_chunk:
                                chunks.append("\n\n".join(current_list_chunk))
                        else:
                            # For other large elements, split by size with header context
                            headers = get_header_hierarchy(text, start)
                            header_text = format_headers(headers) if headers else ""
                            
                            # Split content into chunks of appropriate size
                            for i in range(0, len(content), chunk_size - len(header_text) - 2):
                                chunk_content = content[i:i + chunk_size - len(header_text) - 2]
                                if header_text:
                                    chunks.append(header_text + "\n\n" + chunk_content)
                                else:
                                    chunks.append(chunk_content)
                    
                    # Reset for the next element
                    current_chunk = []
                    current_size = 0
                else:
                    # Normal case: save current chunk and start a new one
                    chunks.append("\n\n".join(current_chunk))
                    
                    # Start new chunk with header context
                    headers = get_header_hierarchy(text, start)
                    if headers:
                        header_text = format_headers(headers)
                        current_chunk = [header_text]
                        current_size = len(header_text)
                    else:
                        current_chunk = []
                        current_size = 0
                    
                    # Add the element to the new chunk
                    current_chunk.append(content)
                    current_size += len(content) + 2
            else:
                # Element fits in current chunk
                current_chunk.append(content)
                current_size += len(content) + 2
        
        last_position = end
    
    # Process any remaining text
    if last_position < len(text):
        remaining_text = text[last_position:].strip()
        if remaining_text:
            # Split remaining text into paragraphs
            paragraphs = re.split(r'\n\n+', remaining_text)
            for paragraph in paragraphs:
                paragraph = paragraph.strip()
                if not paragraph:
                    continue
                
                # If adding this paragraph would exceed chunk_size, start a new chunk
                if current_size + len(paragraph) + 2 > chunk_size and current_chunk:
                    chunks.append("\n\n".join(current_chunk))
                    
                    # Start new chunk with header context
                    headers = get_header_hierarchy(text, last_position)
                    if headers:
                        header_text = format_headers(headers)
                        current_chunk = [header_text]
                        current_size = len(header_text)
                    else:
                        current_chunk = []
                        current_size = 0
                
                # Add paragraph to current chunk
                current_chunk.append(paragraph)
                current_size += len(paragraph) + 2
    
    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    
    # Apply chunk overlap by adding context from previous chunks
    if chunk_overlap > 0 and len(chunks) > 1:
        overlapped_chunks = [chunks[0]]
        
        for i in range(1, len(chunks)):
            prev_chunk = chunks[i-1]
            current_chunk = chunks[i]
            
            # Check if the current chunk already starts with headers
            has_headers = bool(header_pattern.match(current_chunk))
            
            # If the current chunk doesn't start with headers, add context from the previous chunk
            if not has_headers:
                # Extract headers from the previous chunk
                headers = []
                for match in header_pattern.finditer(prev_chunk):
                    level = len(match.group(1))
                    content = match.group(2).strip()
                    
                    # Keep only headers of higher levels
                    headers = [h for h in headers if h[0] < level]
                    headers.append((level, content))
                
                # If we found headers, add them to the current chunk
                if headers:
                    header_text = format_headers(headers)
                    current_chunk = header_text + "\n\n" + current_chunk
            
            overlapped_chunks.append(current_chunk)
        
        return overlapped_chunks
    
    return chunks


# Function to process markdown files
def process_markdown_files(markdown_dir):
    """Process all markdown files in a directory."""
    # Check if directory exists
    if not os.path.exists(markdown_dir):
        print(f"Directory {markdown_dir} does not exist.")
        return [], []
    
    # Get all markdown files
    markdown_files = [f for f in os.listdir(markdown_dir) if f.endswith('.md')]
    print(f"Found {len(markdown_files)} markdown files in {markdown_dir}")
    
    all_chunks = []
    all_metadata = []
    
    # Process each file
    for file_name in tqdm(markdown_files, desc=f"Processing {markdown_dir}"):
        file_path = os.path.join(markdown_dir, file_name)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title from filename or first header
            title = os.path.splitext(file_name)
            first_header_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if first_header_match:
                title = first_header_match.group(1).strip()
            
            # Create chunks
            file_chunks = create_chunks(content)
            
            # Add chunks and metadata
            for i, chunk in enumerate(file_chunks):
                all_chunks.append(chunk)
                
                # Create metadata for this chunk
                metadata = {
                    'source': markdown_dir,
                    'file_name': file_name,
                    'title': title,
                    'chunk_index': i,
                    'total_chunks': len(file_chunks)
                }
                
                # Extract headers for better context
                headers = []
                for match in re.finditer(r'^(#{1,6})\s+(.+)$', chunk, re.MULTILINE):
                    level = len(match.group(1))
                    header_text = match.group(2).strip()
                    headers.append((level, header_text))
                
                if headers:
                    metadata['headers'] = headers
                
                all_metadata.append(metadata)
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return all_chunks, all_metadata

# Function to generate embeddings
def generate_embeddings(chunks, api_token, batch_size=10):
    """Generate embeddings for text chunks using aiproxy."""
    if not api_token:
        print("API token not provided. Cannot generate embeddings.")
        return []
    
    print(f"Generating embeddings for {len(chunks)} chunks with batch size {batch_size}")
    
    embeddings = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:min(i+batch_size, len(chunks))]
        print(f"Processing batch {i//batch_size + 1}/{(len(chunks) + batch_size - 1)//batch_size}")
        
        headers = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
        payload = {"model": "text-embedding-3-small", "input": batch}
        
        try:
            response = requests.post("https://aiproxy.sanand.workers.dev/embeddings", 
                                    headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                batch_embeddings = [item["embedding"] for item in result["data"]]
                embeddings.extend(batch_embeddings)
            else:
                print(f"Error: {response.status_code}, {response.text}")
                # Add empty embeddings as placeholders
                embeddings.extend([[0.0] * 1536 for _ in batch])
        except Exception as e:
            print(f"Exception: {e}")
            # Add empty embeddings as placeholders
            embeddings.extend([[0.0] * 1536 for _ in batch])
        
        # Respect rate limits
        time.sleep(1)
    
    return embeddings

# Function to save embeddings
def save_embeddings(embeddings, chunks, metadata, output_file):
    """Save embeddings, chunks, and metadata to a compressed NumPy file."""
    # Convert embeddings to a NumPy array
    embeddings_array = np.array(embeddings, dtype=np.float32)
    
    # Convert chunks to a NumPy array of objects
    chunks_array = np.array(chunks, dtype=object)
    
    # Convert metadata to JSON string
    metadata_json = json.dumps(metadata)
    
    # Save to compressed NumPy file
    np.savez_compressed(
        output_file,
        embeddings=embeddings_array,
        chunks=chunks_array,
        metadata=metadata_json
    )
    
    print(f"Saved {len(embeddings)} embeddings to {output_file}")
    print(f"File size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")

# Main workflow
def main():
    # Process markdown files from both directories
    print("Processing discourse markdown files...")
    discourse_chunks, discourse_metadata = process_markdown_files(DISCOURSE_DIR)
    
    print("Processing TDS course page markdown files...")
    tds_chunks, tds_metadata = process_markdown_files(TDS_PAGES_DIR)
    
    # Combine chunks and metadata
    all_chunks = discourse_chunks + tds_chunks
    all_metadata = discourse_metadata + tds_metadata
    
    print(f"Total chunks to process: {len(all_chunks)}")
    
    # Generate embeddings
    print("Generating embeddings...")
    all_embeddings = generate_embeddings(all_chunks, API_TOKEN)
    
    # Save everything to a compressed file
    print("Saving embeddings...")
    save_embeddings(all_embeddings, all_chunks, all_metadata, OUTPUT_FILE)
    
    print(f"Done! Embeddings saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
