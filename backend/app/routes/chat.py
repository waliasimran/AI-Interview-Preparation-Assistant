from fastapi import APIRouter, HTTPException
from app.models.schemas import AskRequest, AskResponse
from app.services.rag_service import ask_question

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask_question_route(payload: AskRequest):
    try:
        result = ask_question(payload.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))