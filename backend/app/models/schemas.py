from pydantic import BaseModel
from typing import List, Optional


class AskRequest(BaseModel):
    question: str


class SourceChunk(BaseModel):
    text: str
    document_type: str
    page: Optional[int] = None


class AskResponse(BaseModel):
    answer: str
    sources: List[SourceChunk]


class AnalysisResponse(BaseModel):
    matching_skills: List[str]
    missing_skills: List[str]
    resume_improvements: List[str]
    best_matching_projects: List[str]


class InterviewQuestionsResponse(BaseModel):
    technical_questions: List[str]
    hr_questions: List[str]
    project_questions: List[str]
    follow_up_questions: List[str]


class TellMeResponse(BaseModel):
    answer: str