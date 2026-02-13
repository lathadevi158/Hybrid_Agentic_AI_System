from functools import lru_cache
from app.services.llm import get_llm
from app.services.vector_store import get_static_store
from app.services.db import get_engine


@lru_cache()
def get_llm_dependency():
    return get_llm()


@lru_cache()
def get_vector_store_dependency():
    return get_static_store()


@lru_cache()
def get_db_engine_dependency():
    return get_engine()
