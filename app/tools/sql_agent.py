from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
from app.services.db import get_engine

def get_sql_agent():
    engine = get_engine()
    db = SQLDatabase(engine)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        verbose=False
    )

    return agent


def run_sql_agent(question: str):
    agent = get_sql_agent()
    return agent.run(question)
