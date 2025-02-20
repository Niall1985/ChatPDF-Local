import numpy as np
import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_query(query, pdf_index):
    results = []
    query_embedding = model.encode(query)

    for filename, data in pdf_index.items():
        if len(data) != 4:
            print(f"Warning: Skipping {filename} - Expected 4 elements but got {len(data)}")
            continue
        
        vectorizer, tfidf_matrix, chunks, embeddings = data

        similarities = cosine_similarity([query_embedding], embeddings)[0]

        best_index = np.argmax(similarities)
        best_chunk = chunks[best_index]
        best_similarity = similarities[best_index]  # Capture similarity score

        results.append((filename, best_chunk, best_similarity, best_index))

    return results

def evaluate_results(results):
    """
    Evaluates the results and finds the most relevant content.
    Returns the filename, the most relevant chunk, and its index.
    """
    if not results:
        return None, None, None

    # Sort by similarity score in descending order (most relevant first)
    results.sort(key=lambda x: x[2], reverse=True)
    
    most_relevant = results[0]  # Top result
    return most_relevant[0], most_relevant[1], most_relevant[3]  # (filename, chunk, index)

def humanize_response(text):
    opening_phrases = [
        "That's a great question! Based on what I found,",
        "Here's something useful from your documents:",
        "According to the uploaded PDFs,"
    ]
    ending_phrases = [
        "Does this help?",
        "Let me know if you'd like more details!",
        "I hope you find this useful!"
    ]
    return f"{random.choice(opening_phrases)} {text} {random.choice(ending_phrases)}"
