from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from app.services.embeddings import get_embeddings
import os

VECTOR_PATH = "app/vector_store/static_index"

def build_static_index():
    embeddings = get_embeddings()
    docs = []

    for file in os.listdir("data/static_pdfs"):
        loader = PyPDFLoader(f"data/static_pdfs/{file}")
        docs.extend(loader.load())

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(VECTOR_PATH)


def retrieve_from_static(query):
    embeddings = get_embeddings()
    vectorstore = FAISS.load_local(VECTOR_PATH, embeddings)
    docs = vectorstore.similarity_search(query, k=3)
    return docs
