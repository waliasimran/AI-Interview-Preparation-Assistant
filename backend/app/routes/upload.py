import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.config import UPLOAD_DIR, FAISS_INDEX_DIR
from app.services.pdf_loader import load_pdf, load_text_file
from app.services.text_splitter import split_documents
from app.services.embeddings import get_embeddings
from app.services.vector_store import create_and_save_vectorstore

router = APIRouter()


def save_uploaded_file(upload_file: UploadFile, destination_path: str):
    with open(destination_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)


@router.post("/upload-documents")
async def upload_documents(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    try:
        resume_path = os.path.join(UPLOAD_DIR, resume.filename)
        jd_path = os.path.join(UPLOAD_DIR, job_description.filename)

        save_uploaded_file(resume, resume_path)
        save_uploaded_file(job_description, jd_path)

        # Load resume
        if resume.filename.lower().endswith(".pdf"):
            resume_docs = load_pdf(resume_path)
        elif resume.filename.lower().endswith(".txt"):
            resume_docs = load_text_file(resume_path, "resume")
        else:
            raise HTTPException(status_code=400, 
                                detail="Resume must be PDF or TXT")

        # Load JD
        if job_description.filename.lower().endswith(".pdf"):
            jd_docs = load_pdf(jd_path)
        elif job_description.filename.lower().endswith(".txt"):
            jd_docs = load_text_file(jd_path, "job_description")
        else:
            raise HTTPException(status_code=400, 
                                detail="Job description must be PDF or TXT")

        # Add metadata
        for doc in resume_docs:
            doc.metadata["document_type"] = "resume"

        for doc in jd_docs:
            doc.metadata["document_type"] = "job_description"

        all_docs = resume_docs + jd_docs
        chunks = split_documents(all_docs)

        embeddings = get_embeddings()
        create_and_save_vectorstore(chunks, embeddings, FAISS_INDEX_DIR)

        return {
            "message": "Documents uploaded and processed successfully.",
            "resume_filename": resume.filename,
            "job_description_filename": job_description.filename,
            "total_documents": len(all_docs),
            "total_chunks": len(chunks)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))