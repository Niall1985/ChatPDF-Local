import streamlit as st
from backend.text_extractor import text_extractor
from backend.text_processing import build_index
from backend.search_engine import search_query, humanize_response, evaluate_results
from nltk.tokenize import word_tokenize
from backend.summarizer import summarizer

st.set_page_config(page_title="📄 AI PDF Chat", layout="wide")
st.title("📄 AI Chat with Multiple PDFs")
st.write("Upload multiple PDFs and chat with them!")

uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing PDFs..."):
        pdf_texts, texts = text_extractor(uploaded_files)
        pdf_indexes = build_index(pdf_texts)
        st.success("PDFs loaded successfully! ✅")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Separate summarization from queries
    if st.button("Summarize PDFs"):
        with st.spinner("Summarizing..."):
            summary = summarizer(texts)
            st.session_state.chat_history.append(("🤖 **Assistant:**", summary))
    
    # Normal query processing
    user_query = st.text_input("Ask a question about the PDFs:")

    if user_query:
        st.session_state.chat_history.append(("👤 **User:**", user_query))
        best_results = search_query(user_query, pdf_indexes)
        filename, best_chunk, best_index = evaluate_results(best_results)

        if filename:
            humanized_response = humanize_response(best_chunk)
            response_message = f"📄 **Source: {filename}**\n\n\n{humanized_response}"
            st.session_state.chat_history.append(("🤖 **Assistant:**", response_message))
        else:
            st.session_state.chat_history.append(("🤖 **Assistant:**", "⚠️ No relevant content found."))

    for role, message in st.session_state.chat_history:
        with st.chat_message(role.split("**")[1].lower()): 
            st.markdown(f"{role} {message}")
