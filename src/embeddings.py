from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import EMBEDDING_MODEL

load_dotenv()


def get_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    return embeddings