from backend.core import run_llm
import streamlit as st
import time
from streamlit_chat import message
import os

os.environ["OPENAI_API_KEY"] = "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"

st.header("Fawry Documentation Helper Bot.")

prompt = st.text_input("Prompt", placeholder="Enter your prompt...")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if prompt:
    with st.spinner("Generating response..."):
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )
        formatted_response = f"{generated_response['answer']}"

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append((prompt, generated_response["answer"]))

    if st.session_state["user_prompt_history"]:
        for generated_response, user_query in zip(
            st.session_state["chat_answers_history"],
            st.session_state["user_prompt_history"],
        ):
            message(user_query, is_user=True)
            message(generated_response)
