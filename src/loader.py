import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from src.config import DATA_FOLDER


def load_documents():
    all_documents = []

    for file_name in os.listdir(DATA_FOLDER):
        file_path = os.path.join(DATA_FOLDER, file_name)

        if file_name.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            all_documents.extend(documents)
            print("Loaded PDF:", file_name, "-", len(documents), "pages")


    return all_documents