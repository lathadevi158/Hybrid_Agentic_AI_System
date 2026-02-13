from langchain.vectorstores import FAISS
from app.services.embeddings import get_embeddings
import os

STATIC_INDEX_PATH = "data/vector_index"

_embeddings = get_embeddings()


def build_static_index(documents):
    """
    Build static knowledge base index.
    Run this offline.
    """
    vectorstore = FAISS.from_documents(documents, _embeddings)
    vectorstore.save_local(STATIC_INDEX_PATH)


def get_static_store():
    """
    Load static knowledge base.
    """
    if not os.path.exists(STATIC_INDEX_PATH):
        raise RuntimeError("Static index not found. Build it first.")

    return FAISS.load_local(STATIC_INDEX_PATH, _embeddings)


def create_session_store(documents):
    """
    Create temporary in-memory store for uploaded documents.
    """
    return FAISS.from_documents(documents, _embeddings)
