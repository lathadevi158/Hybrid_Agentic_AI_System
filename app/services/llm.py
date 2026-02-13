from langchain.chat_models import ChatOpenAI
from app.config import LLM_MODEL

def get_llm():
    return ChatOpenAI(model=LLM_MODEL, temperature=0)
