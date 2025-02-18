import streamlit as st
from backend.text_extractor import text_extractor
from backend.text_processing import build_index
from backend.search_engine import search_query, humanize_response

st.set_page_config(page_title="📄 AI PDF Chat", layout="wide")
st.title("📄 AI Chat with Multiple PDFs")
st.write("Upload multiple PDFs and chat with them!")

# File uploader (Allow multiple PDFs)
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing PDFs..."):
        pdf_texts = text_extractor(uploaded_files)
        pdf_indexes = build_index(pdf_texts)
        st.success("PDFs loaded successfully! ✅")

    # Chat History
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User query input
    user_query = st.text_input("Ask a question about the PDFs:")

    if user_query:
        st.session_state.chat_history.append(("👤 **User:**", user_query))  # User message
        best_results = search_query(user_query, pdf_indexes)

        for filename, best_chunk in best_results:
            humanized_response = humanize_response(best_chunk)
            st.session_state.chat_history.append(("🤖 **Assistant:**", f"📄 **Source: {filename}**\n\n{humanized_response}"))

    # Display chat history
    for role, message in st.session_state.chat_history:
        with st.chat_message(role.split("**")[1].lower()):  # Format for chat UI
            st.markdown(f"{role} {message}")
