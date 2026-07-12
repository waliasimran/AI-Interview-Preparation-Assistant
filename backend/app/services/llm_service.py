from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY, MODEL_NAME


def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=MODEL_NAME,
        temperature=0.2
    )