import axios from "axios";

const API = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}/api`,
});

export const uploadDocuments = async (resumeFile, jdFile) => {
  const formData = new FormData();
  formData.append("resume", resumeFile);
  formData.append("job_description", jdFile);

  const response = await API.post("/upload-documents", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export const askQuestion = async (question) => {
  const response = await API.post("/ask", { question });
  return response.data;
};

export const analyzeResume = async () => {
  const response = await API.get("/analyze");
  return response.data;
};

export const generateInterviewQuestions = async () => {
  const response = await API.get("/generate-interview-questions");
  return response.data;
};

export const generateTellMe = async () => {
  const response = await API.get("/tell-me-about-yourself");
  return response.data;
};