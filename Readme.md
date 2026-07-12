# AI Interview Prep Assistant

AI Interview Prep Assistant is a **RAG-based GenAI web application** that helps users prepare for job applications and interviews by analyzing their **resume** against a **job description**.  
The system allows users to upload both documents, retrieve relevant information using **vector search**, and generate tailored outputs such as resume analysis, interview questions, and introduction content.

---

## Features

### 1. Resume & Job Description Upload
- Upload a **resume PDF** and a **job description PDF**
- Extracts text from both documents
- Splits content into smaller chunks for retrieval

### 2. RAG-based Question Answering
- Uses **Retrieval-Augmented Generation (RAG)** to answer user questions based on the uploaded documents
- Retrieves the most relevant chunks from the resume and job description before generating the response
- Helps users ask questions like:
  - *What skills are missing in my resume for this role?*
  - *How well does my resume match the job description?*
  - *Which projects in my resume are most relevant for this role?*

### 3. Resume vs Job Description Analysis
Generates a structured analysis including:
- **Matching skills**
- **Missing skills**
- **Resume strengths**
- **Improvement suggestions**
- **Overall alignment with the role**

### 4. Interview Question Generation
Creates interview questions tailored to the uploaded resume and job description, including:
- Technical questions
- Project-based questions
- Behavioral questions
- Role-specific questions

### 5. Tell Me About Yourself Generator
Generates a customized **“Tell me about yourself”** response based on:
- the user’s resume
- the target job description
- relevant skills and projects

---

## Tech Stack

### Frontend
- **React (Vite)**
- CSS for UI styling
- Axios for API integration

### Backend
- **FastAPI**
- Python

### GenAI / RAG
- **LangChain**
- **FAISS** for vector storage and retrieval
- **Sentence Transformers / Embeddings**
- **LLM API** for generation

---

## How It Works

1. User uploads a **resume** and **job description**
2. The backend:
   - extracts text from both PDFs
   - splits text into chunks
   - converts chunks into embeddings
   - stores them in **FAISS vector store**
3. When the user asks a question:
   - the query is converted into an embedding
   - the most relevant chunks are retrieved from the vector store
   - the retrieved context is passed to the LLM
4. The LLM generates a contextual response based on the uploaded documents

---

## Project Workflow

### Upload Stage
- Resume PDF and JD PDF are uploaded through the frontend
- Backend processes the documents and stores chunk embeddings in FAISS

### Retrieval Stage
- User question is embedded
- Similar chunks are fetched from the vector store

### Generation Stage
- Retrieved chunks are passed to the LLM
- The model generates:
  - answers to user questions
  - resume analysis
  - interview questions
  - self-introduction content

---

## Example Use Cases

- Check whether a resume matches a specific job description
- Identify missing skills before applying for a role
- Prepare role-specific interview questions
- Build a personalized “Tell me about yourself” answer
- Understand which resume projects align best with a target job

---

## Folder Structure

```bash
AI-Interview-Prep-Assistant/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── main.py
│   ├── data/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
└── README.md