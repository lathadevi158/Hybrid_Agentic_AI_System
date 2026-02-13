from app.services.memory_store import get_memory
from app.core.logging import get_logger

logger = get_logger(__name__)


def memory_node(state: dict):
    """
    Injects conversation history into agent state.
    """

    session_id = state.get("session_id")

    if not session_id:
        logger.warning("No session_id provided in state.")
        return state

    history = get_memory(session_id)

    logger.info(f"Loaded memory for session {session_id} | Messages: {len(history)}")

    return {
        **state,
        "history": history
    }
