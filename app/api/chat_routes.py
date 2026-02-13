from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.orchestrator.graph import build_graph
from app.core.logging import get_logger
from app.core.exceptions import ApplicationException
from app.core.security import detect_prompt_injection
from app.services.memory_store import save_memory
from datetime import datetime
import asyncio

router = APIRouter()
logger = get_logger(__name__)

graph = build_graph()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    logger.info(f"Session: {request.session_id} | Question: {request.question}")

    if detect_prompt_injection(request.question):
        raise ApplicationException("Security violation detected")

    try:
        result = graph.invoke({
            "question": request.question,
            "session_id": request.session_id
        })

        save_memory(request.session_id, {
            "question": request.question,
            "answer": result["answer"]
        })

        return ChatResponse(
            session_id=request.session_id,
            answer=result["answer"],
            timestamp=datetime.utcnow()
        )

    except Exception as e:
        logger.error(f"Chat processing failed: {str(e)}")
        raise


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    if detect_prompt_injection(request.question):
        raise ApplicationException("Security violation detected")

    async def generate():
        result = graph.invoke({
            "question": request.question,
            "session_id": request.session_id
        })

        for token in result["answer"]:
            yield token
            await asyncio.sleep(0.01)

    return StreamingResponse(generate(), media_type="text/plain")
