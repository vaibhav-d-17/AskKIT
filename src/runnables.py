import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from src.config import LLM_MODEL
from src.prompt import prompt
from src.retriever import get_retriever

load_dotenv()

llm = ChatGoogleGenerativeAI(model=LLM_MODEL, temperature=0)
retriever = get_retriever()
chain = prompt | llm | StrOutputParser()


def format_docs(docs):
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n\n"
    return text


def get_sources(docs):
    sources = []
    for doc in docs:
        file_name = os.path.basename(doc.metadata["source"])
        page = doc.metadata.get("page_label")
        if page is None:
            source_text = file_name
        else:
            source_text = file_name + " (page " + str(page) + ")"
        if source_text not in sources:
            sources.append(source_text)
    return sources


def ask_question(question):
    docs = retriever.invoke(question)
    context = format_docs(docs)
    answer = chain.invoke({"context": context, "question": question})
    sources = get_sources(docs)
    return answer, sources