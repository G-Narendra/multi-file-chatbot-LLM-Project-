import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFacePipeline
from src.retrieval import retrieve_relevant_chunks
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

load_dotenv()

LLM_MODEL_NAME = os.getenv("MODEL_NAME", "google/flan-t5-base")

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(LLM_MODEL_NAME)
text_gen = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)
llm = HuggingFacePipeline(pipeline=text_gen)
memory = ConversationBufferMemory()

def get_chat_response(query, vector_store):
    relevant_chunks = retrieve_relevant_chunks(query, vector_store)
    context = "\n".join(relevant_chunks)

    prompt = f"Context:\n{context}\n\nUser Query: {query}\n\nAnswer:"
    response = llm.invoke(prompt)

    memory.save_context({"query": query}, {"response": response})
    return response
