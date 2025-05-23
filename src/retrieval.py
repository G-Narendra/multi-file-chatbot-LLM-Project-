
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vector_store


def retrieve_relevant_chunks(query, vector_store, k=3):
    """Retrieve top-k relevant chunks using FAISS."""
    results = vector_store.similarity_search(query, k=k)
    return [result.page_content for result in results]
