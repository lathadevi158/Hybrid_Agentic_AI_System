from langgraph.graph import StateGraph
from app.orchestrator.router_node import router_node
from app.tools.sql_agent import run_sql_agent
from app.tools.static_rag import run_static_rag
from app.orchestrator.response_node import generate_response

class AgentState(dict):
    pass

def sql_node(state):
    result = run_sql_agent(state["question"])
    return {"context": result}

def static_node(state):
    result = run_static_rag(state["question"])
    return {"context": result}

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("router", router_node)
    graph.add_node("sql", sql_node)
    graph.add_node("static", static_node)
    graph.add_node("response", generate_response)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        lambda s: s["route"],
        {
            "SQL": "sql",
            "STATIC_DOC": "static",
            "HYBRID": "sql"
        }
    )

    graph.add_edge("sql", "response")
    graph.add_edge("static", "response")

    graph.set_finish_point("response")

    return graph.compile()
