from app.services.vector_store import get_static_store

def run_static_rag(question: str):
    vectorstore = get_static_store()
    docs = vectorstore.similarity_search(question, k=5)
    return "\n".join([d.page_content for d in docs])
