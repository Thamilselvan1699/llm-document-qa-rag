from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from src.load_docs import load_documents
from src.embed_store import create_vector_store

def answer_question(question):
    docs = load_documents()
    vectorstore = create_vector_store(docs)
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        retriever=vectorstore.as_retriever()
    )
    return qa.run(question)
