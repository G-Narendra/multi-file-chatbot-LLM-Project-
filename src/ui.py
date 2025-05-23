import streamlit as st
from src.file_processing import process_files
from src.chunking import chunk_text
from src.retrieval import create_vector_store
from src.chatbot import get_chat_response


st.set_page_config(page_title="Multi-File Chatbot", layout="wide")

with st.sidebar:
    st.header("📂 Upload Files")
    uploaded_files = st.file_uploader(
        "Upload PDFs, TXTs, CSVs, XLSX", 
        type=["pdf", "txt", "csv", "xlsx"], 
        accept_multiple_files=True
    )
    if uploaded_files:
        raw_documents = process_files(uploaded_files)
        chunks = [chunk_text(doc) for doc in raw_documents]
        vector_store = create_vector_store([chunk for sublist in chunks for chunk in sublist])
        st.success(f"✅ Loaded {len(raw_documents)} document(s) successfully!")

st.title("🤖 Multi-File Chatbot")

col1, col2, col3 = st.columns([1, 2, 1])  # Center-align main content

with col2:
    st.subheader("Ask a question about your documents:")
    user_query = st.text_input("")

    if user_query and uploaded_files:
        response = get_chat_response(user_query, vector_store)
        st.markdown("**💬 Chatbot Answer:**")
        st.info(response)
