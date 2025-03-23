import streamlit as st
from response_generator import generate_response
from text_processing import files_for_processing

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_files = st.file_uploader('Upload PDF files', accept_multiple_files=True, type=["pdf"])

if uploaded_files:
    with st.spinner("Processing PDFs..."):
        content = files_for_processing(uploaded_files) 
else:
    content = "" 

user_query = st.text_input("Your prompt:")

if user_query:
    st.session_state.chat_history.append(("user", f"👤 **User:** {user_query}"))

    response = generate_response(user_query, content) if content else "⚠️ No document uploaded."
    
    st.session_state.chat_history.append(("assistant", f"🤖 **Assistant:** {response}"))

for role, message in st.session_state.chat_history:
    with st.chat_message(role):  
        st.markdown(message)
