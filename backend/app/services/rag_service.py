from app.config import FAISS_INDEX_DIR
from app.services.embeddings import get_embeddings
from app.services.vector_store import load_vectorstore
from app.services.llm_service import get_llm
from app.services.prompts import (
    QA_PROMPT,
    ANALYSIS_PROMPT,
    INTERVIEW_QUESTIONS_PROMPT,
    TELL_ME_PROMPT
)
from app.services.helper_service import parse_section_items


def get_retrieved_docs(question: str, k: int = 4):
    embeddings = get_embeddings()
    vectorstore = load_vectorstore(FAISS_INDEX_DIR, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    docs = retriever.invoke(question)
    return docs


def build_context_from_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


def format_sources(docs):
    sources = []
    for doc in docs:
        sources.append({
            "text": doc.page_content[:500],
            "document_type": doc.metadata.get("document_type", "unknown"),
            "page": doc.metadata.get("page")
        })
    return sources


def ask_question(question: str):
    docs = get_retrieved_docs(question, k=4)
    context = build_context_from_docs(docs)
    llm = get_llm()

    prompt = QA_PROMPT.format(context=context, question=question)
    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": format_sources(docs)
    }


def analyze_resume_vs_jd():
    # Generic question to pull both resume and JD related chunks
    docs = get_retrieved_docs(
        "Analyze the resume against the job description and identify "
        "matching and missing skills.", k=8)
    context = build_context_from_docs(docs)
    llm = get_llm()

    prompt = ANALYSIS_PROMPT.format(context=context)
    response = llm.invoke(prompt)
    text = response.content

    return {
        "matching_skills": parse_section_items(text, "MATCHING_SKILLS:"),
        "missing_skills": parse_section_items(text, "MISSING_SKILLS:"),
        "resume_improvements": parse_section_items
        (text, "RESUME_IMPROVEMENTS:"),
        "best_matching_projects": parse_section_items
        (text, "BEST_MATCHING_PROJECTS:")
    }


def generate_interview_questions():
    docs = get_retrieved_docs(
        "Generate interview questions based on the resume and job description",
        k=8
    )
    context = build_context_from_docs(docs)
    llm = get_llm()

    prompt = INTERVIEW_QUESTIONS_PROMPT.format(context=context)
    response = llm.invoke(prompt)
    text = response.content

    return {
        "technical_questions": 
        parse_section_items(text, "TECHNICAL_QUESTIONS:"),
        "hr_questions": parse_section_items(text, "HR_QUESTIONS:"),
        "project_questions": parse_section_items(text, "PROJECT_QUESTIONS:"),
        "follow_up_questions": 
        parse_section_items(text, "FOLLOW_UP_QUESTIONS:")
    }


def generate_tell_me_about_yourself():
    docs = get_retrieved_docs(
        "Write a tell me about yourself "
        "answer based on the resume and job description.", k=8)
    context = build_context_from_docs(docs)
    llm = get_llm()

    prompt = TELL_ME_PROMPT.format(context=context)
    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }