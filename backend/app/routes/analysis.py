from fastapi import APIRouter, HTTPException
from app.models.schemas import AnalysisResponse, TellMeResponse
from app.services.rag_service import (
    analyze_resume_vs_jd, 
    generate_tell_me_about_yourself,
)

router = APIRouter()


@router.get("/analyze", response_model=AnalysisResponse)
def analyze_route():
    try:
        result = analyze_resume_vs_jd()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tell-me-about-yourself", response_model=TellMeResponse)
def tell_me_route():
    try:
        result = generate_tell_me_about_yourself()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))