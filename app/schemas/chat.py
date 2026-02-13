from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ChatRequest(BaseModel):
    session_id: str = Field(..., description="Unique session identifier")
    question: str = Field(..., min_length=3, description="User query")
    metadata: Optional[dict] = Field(default=None, description="Optional client metadata")


class ChatResponse(BaseModel):
    session_id: str
    answer: str
    sources: Optional[List[str]] = None
    tokens_used: Optional[int] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
