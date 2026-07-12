from fastapi import APIRouter, HTTPException
from app.models.schemas import InterviewQuestionsResponse
from app.services.rag_service import generate_interview_questions

router = APIRouter()


@router.get("/generate-interview-questions", 
            response_model=InterviewQuestionsResponse)
def generate_interview_questions_route():
    try:
        result = generate_interview_questions()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))