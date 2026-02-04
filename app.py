import streamlit as st
from src.load_docs import load_documents
from src.embed_store import create_vector_store
from src.rag_pipeline import generate_answer

st.title("LLM Document Q&A System")

docs = load_documents("data/documents")
vector_store = create_vector_store(docs)

query = st.text_input("Ask a question based on documents")

if query:
    answer = generate_answer(query, vector_store)
    st.write(answer)
