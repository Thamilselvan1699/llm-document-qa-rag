from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(documents):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(documents, embeddings)
