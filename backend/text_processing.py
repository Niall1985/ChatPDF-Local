import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


def chunk_text(text, chunck_size=500):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current_chunk = [], ""
    for sentence in sentences:
        if len(sentence) + len(current_chunk) <= chunck_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    chunks.append(current_chunk.strip())
    return chunks


def build_index(pdf_text):
    pdf_index = {}
    for filename, text in pdf_text.items():
        chunks = chunk_text(text)
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(chunks)
        embeddings = [model.encode(chunk) for chunk in chunks]  # Generate embeddings
        pdf_index[filename] = (vectorizer, tfidf_matrix, chunks, embeddings)  # Store 4 elements
    return pdf_index