# LLM-Powered Document Q&A System (RAG)

This project implements a Retrieval-Augmented Generation (RAG) system that allows users
to ask questions over a set of documents using Large Language Models.

## Architecture
Documents → Chunking → Embeddings → Vector Store → Retrieval → LLM Answer

## Tech Stack
- Python
- LangChain
- OpenAI API
- FAISS
- Streamlit

## How It Works
1. Documents are loaded and converted into embeddings
2. Embeddings are stored in a FAISS vector database
3. Relevant documents are retrieved based on user query
4. LLM generates an answer grounded in retrieved context

## Limitations
- Depends on embedding quality
- Not suitable for real-time large-scale data
- Requires API key for LLM access

## Future Improvements
- Add PDF support
- Improve chunking logic
- Add authentication
