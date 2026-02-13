from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from app.services.embeddings import get_embeddings
import tempfile

def create_session_index(file):
    embeddings = get_embeddings()

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        loader = PyPDFLoader(tmp.name)
        docs = loader.load()

    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


def retrieve_from_upload(vectorstore, query):
    return vectorstore.similarity_search(query, k=3)
