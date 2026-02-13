from app.services.llm import get_llm
from app.services.memory_store import get_memory

def generate_response(state):
    llm = get_llm()

    history = get_memory(state["session_id"])

    prompt = f"""
Conversation History:
{history}

Context:
{state.get("context","")}

User Question:
{state["question"]}

Provide a structured and accurate answer.
"""

    answer = llm.invoke(prompt).content
    return {"answer": answer}
