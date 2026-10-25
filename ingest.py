from src.loader import load_documents
from src.chunker import split_documents
from src.vectorstore import build_vectorstore

documents = load_documents()
chunks = split_documents(documents)
print("Chunks to store:", len(chunks))

build_vectorstore(chunks)
print("Done. Index is ready in the chroma_db folder.")