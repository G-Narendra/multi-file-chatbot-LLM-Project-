import streamlit as st
from src.file_processing import process_files
from src.chunking import chunk_text
from src.retrieval import create_vector_store
from src.chatbot import get_chat_response

st.set_page_config(page_title="📄 Multi-File Chatbot")
st.title("📄 Multi-File Chatbot")

uploaded_files = st.file_uploader(
    "Upload files (PDF, TXT, CSV, XLSX)",
    type=["pdf", "txt", "csv", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Processing documents..."):
        raw_documents = process_files(uploaded_files)
        chunks = [chunk_text(doc) for doc in raw_documents]
        flat_chunks = [chunk for sublist in chunks for chunk in sublist if chunk.strip()]

        if not flat_chunks:
            st.error("No valid text content found in the uploaded files.")
        else:
            vector_store = create_vector_store(flat_chunks)
            st.success(f"Loaded {len(raw_documents)} document(s) successfully!")

            query = st.text_input("Ask a question about your documents:")

            if query:
                with st.spinner("Generating answer..."):
                    print("Query:", query)
                    print("Vector store type:", type(vector_store))
                    answer = get_chat_response(query, vector_store)
                    st.markdown("### Answer")
                    st.write(answer)
