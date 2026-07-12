from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router as upload_router
from app.routes.chat import router as chat_router
from app.routes.analysis import router as analysis_router
from app.routes.interview import router as interview_router

app = FastAPI(title="AI Interview Prep Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api", tags=["Upload"])
app.include_router(chat_router, prefix="/api", tags=["Chat"])
app.include_router(analysis_router, prefix="/api", tags=["Analysis"])
app.include_router(interview_router, prefix="/api", tags=["Interview"])


@app.get("/")
def root():
    return {"message": "AI Interview Prep Assistant Backend is running"}