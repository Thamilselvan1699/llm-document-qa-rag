from langchain_openai import OpenAI

def generate_answer(query, vector_store):
    docs = vector_store.similarity_search(query, k=3)
    context = " ".join([d.page_content for d in docs])

    prompt = f"""
    Answer the question using only the context below.
    Context: {context}
    Question: {query}
    """

    llm = OpenAI(temperature=0)
    return llm(prompt)
