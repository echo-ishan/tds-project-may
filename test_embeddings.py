import os
import json
import numpy as np
import requests
from dotenv import load_dotenv
import argparse
from sklearn.metrics.pairwise import cosine_similarity

# --- Configuration ---
load_dotenv()
API_TOKEN = os.getenv("OPENAI_API_KEY")
AIPROXY_EMBEDDINGS_URL = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
EMBEDDINGS_FILE = "knowledge_embeddings.npz"

def get_query_embedding(text, api_token):
    """Generates an embedding for a single text query using the aiproxy service."""
    if not api_token:
        print("Error: AIPROXY_TOKEN not found.")
        return None

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-embedding-3-small",
        "input": text
    }

    try:
        response = requests.post(AIPROXY_EMBEDDINGS_URL, headers=headers, json=payload, timeout=20)
        if response.status_code == 200:
            return response.json()['data'][0]['embedding']
        else:
            print(f"Error from API: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def test_retrieval(query, top_k=3):
    """Loads embeddings and performs a similarity search for the given query."""
    if not os.path.exists(EMBEDDINGS_FILE):
        print(f"Error: Embeddings file '{EMBEDDINGS_FILE}' not found.")
        return

    # Load the knowledge base
    print(f"Loading knowledge base from '{EMBEDDINGS_FILE}'...")
    data = np.load(EMBEDDINGS_FILE, allow_pickle=True)
    embeddings = data['embeddings']
    chunks = data['chunks']
    metadata = json.loads(data['metadata'].item())
    print(f"✓ Loaded {len(embeddings)} chunks.")

    # Generate embedding for the user's query
    print(f"\nGenerating embedding for your query: '{query}'")
    query_embedding = get_query_embedding(query, API_TOKEN)
    if query_embedding is None:
        print("Could not generate query embedding. Aborting.")
        return

    # Calculate cosine similarity
    # The query_embedding needs to be reshaped to (1, D) for the function
    similarities = cosine_similarity([query_embedding], embeddings)[0]

    # Get the indices of the top_k most similar chunks
    top_k_indices = np.argsort(similarities)[-top_k:][::-1]

    # Display the results
    print("\n--- Top 3 Most Relevant Chunks Found ---")
    for i, index in enumerate(top_k_indices):
        chunk_text = chunks[index]
        meta = metadata[index]
        similarity_score = similarities[index]
        
        print(f"\n--- Result #{i+1} | Similarity: {similarity_score:.4f} ---")
        print(f"Source: {meta['source_dir']}/{meta['file_name']} (Chunk {meta['chunk_index']})")
        print("-" * 20)
        print(chunk_text)
        print("--- End of Result ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test the quality of embeddings via retrieval.")
    parser.add_argument("--query", type=str, required=True, help="The question you want to ask your knowledge base.")
    args = parser.parse_args()
    
    test_retrieval(args.query)
