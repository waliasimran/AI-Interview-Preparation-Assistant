import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs


def load_text_file(file_path: str, document_type: str):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return [
        Document(
            page_content=text,
            metadata={"document_type": document_type, "source": 
                      os.path.basename(file_path)}
        )
    ]