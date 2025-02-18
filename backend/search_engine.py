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

        results.append((filename, best_chunk))

    return results

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
