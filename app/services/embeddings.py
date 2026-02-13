from langchain.embeddings import OpenAIEmbeddings
from app.config import EMBEDDING_MODEL

def get_embeddings():
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)
