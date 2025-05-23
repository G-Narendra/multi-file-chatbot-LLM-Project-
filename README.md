# 📄 Multi-File Chatbot
An intelligent chatbot that allows users to upload multiple document formats (PDFs, TXTs, CSVs) and ask questions across them using Retrieval-Augmented Generation (RAG).

## 🚀 Features
Multi-File Support – Upload PDFs, TXTs, and CSVs dynamically via the sidebar.

Document Parsing – Extracts text seamlessly using PyMuPDF, TextLoader, and CSVLoader.

Chunking & Vector Storage – Uses FAISS for efficient retrieval of document data.

LLM Integration – Powered by open-source Llama 2 from Hugging Face (no OpenAI API required!).

Conversation Memory – Retains chat history for better contextual understanding.

Streamlit UI – Clean interface with sidebar file uploads and a center chat interface.

## 🏗️ Project Structure
```bash
multi_file_chatbot/
│── .env                         # Environment variables (API keys, config settings)
│── .gitignore                   # Files to exclude from Git version control
│── README.md                    # Project overview & setup instructions
│── requirements.txt              # Dependencies list (Streamlit, LangChain, FAISS, etc.)
│── app.py                        # Main Streamlit UI script
│── config.yaml                   # Configuration settings (chunking, embeddings, vector store)
│── data/                         # Temporary storage for uploaded files
│── src/                          # Core project code
│   ├── ui.py                     # Streamlit UI components (file uploader, chat interface)
│   ├── file_processing.py        # File loaders for PDFs, CSVs, TXTs
│   ├── chunking.py               # Text chunking & vector store management
│   ├── retrieval.py              # Retrieval-Augmented Generation (RAG) logic
│   ├── chatbot.py                # Chat handling, memory & response generation
│── models/                        # Pre-trained embeddings & vector storage
│── logs/                          # Directory for chat history logs

```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/multi_file_chatbot.git
cd multi_file_chatbot
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run the chatbot
```bash
streamlit run app.py
```
### 🛠️ Configuration

Modify .env or config.yaml to customize:

Hugging Face model selection (MODEL_NAME).

Chunking parameters (CHUNK_SIZE, CHUNK_OVERLAP).

Vector store location (VECTOR_STORE_PATH).

### 💡 How It Works
Step 1: Upload multiple files via the sidebar.

Step 2: Enter a query in the center chat box.

Step 3: The chatbot retrieves relevant document snippets and generates an answer.

### 🌍 Technologies Used
Streamlit → UI Interface

LangChain → RAG-based retrieval

FAISS → Vector embeddings storage

Hugging Face Transformers → Llama-2 for response generation

PyMuPDF, CSVLoader, TextLoader → Document parsing