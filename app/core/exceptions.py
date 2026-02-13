from fastapi import Request
from fastapi.responses import JSONResponse
from app.schemas.chat import ErrorResponse
from datetime import datetime


class ApplicationException(Exception):
    def __init__(self, message: str, detail: str = None):
        self.message = message
        self.detail = detail
        super().__init__(message)


class SecurityException(ApplicationException):
    pass


class DatabaseException(ApplicationException):
    pass


class LLMServiceException(ApplicationException):
    pass


def application_exception_handler(request: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            error=exc.message,
            detail=exc.detail,
            timestamp=datetime.utcnow()
        ).dict()
    )


def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Internal Server Error",
            detail=str(exc),
            timestamp=datetime.utcnow()
        ).dict()
    )
