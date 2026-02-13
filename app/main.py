from fastapi import FastAPI, UploadFile, File
from app.orchestrator.graph import build_graph
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()
graph = build_graph()

@app.post("/chat")
async def chat(question: str):
    result = graph.invoke({"question": question})
    return {"answer": result["answer"]}


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    async def generate():
        result = graph.invoke({
            "question": request.question,
            "session_id": request.session_id
        })

        for token in result["answer"]:
            yield token
            await asyncio.sleep(0.01)

    return StreamingResponse(generate(), media_type="text/plain")
