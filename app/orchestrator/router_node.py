from app.services.llm import get_llm

ROUTER_PROMPT = """
You are a routing classifier.

Classify the user's query into one of:
- SQL
- STATIC_DOC
- UPLOAD_DOC
- HYBRID

Respond with only the label.
"""

def router_node(state):
    llm = get_llm()

    classification = llm.invoke(
        ROUTER_PROMPT + "\nUser Query:\n" + state["question"]
    ).content.strip()

    return {"route": classification}
