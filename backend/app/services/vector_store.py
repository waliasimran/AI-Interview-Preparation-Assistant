import os
from langchain_community.vectorstores import FAISS


def create_and_save_vectorstore(chunks, embeddings, save_path: str):
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(save_path)
    return vectorstore


def load_vectorstore(save_path: str, embeddings):
    if not os.path.exists(save_path):
        raise FileNotFoundError
    ("FAISS index not found. Please upload documents first.")
    return FAISS.load_local(
        save_path,
        embeddings,
        allow_dangerous_deserialization=True
    )