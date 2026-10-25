import streamlit as st
from src.runnables import ask_question

st.set_page_config(page_title="AskKIT", page_icon="🎓")
st.title("🎓 AskKIT")

# keep the chat history between messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# input box at the bottom
question = st.chat_input("Type your question here")

if question:
    # show the user's question
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({"role": "user", "content": question})

    # get and show the answer
    with st.chat_message("assistant"):
        with st.spinner("Searching college documents..."):
            answer, sources = ask_question(question)
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})