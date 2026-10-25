import os
import shutil
import time
from langchain_chroma import Chroma
from src.config import CHROMA_FOLDER, COLLECTION_NAME
from src.embeddings import get_embeddings

def load_vectorstore():
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_FOLDER,
    )
    return vectorstore

def build_vectorstore(chunks):
    if os.path.exists(CHROMA_FOLDER):
        shutil.rmtree(CHROMA_FOLDER)

    vectorstore = load_vectorstore()

    batch_size = 20
    total = len(chunks)

    for start in range(0, total, batch_size):
        batch = chunks[start:start + batch_size]
        vectorstore.add_documents(batch)
        print("Stored", start + len(batch), "of", total, "chunks")
        time.sleep(15)

    return vectorstore