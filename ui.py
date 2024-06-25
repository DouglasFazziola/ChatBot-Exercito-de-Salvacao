import streamlit as st
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
from time import sleep
from langchain_core.runnables.history import RunnableWithMessageHistory
from llm import KMVAssist 
import streamlit as st
import random
from streamlit.runtime.scriptrunner import get_script_run_ctx
import base64


def main():
    session_id = get_script_run_ctx().session_id

    try:
        st.set_page_config(
            page_title="KMV Assist",
            page_icon="data:image/png;base64,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",
            initial_sidebar_state="collapsed",
            layout="centered",
    )
    except:
        st.experimental_rerun()

    col1,col2 = st.columns([3,4])
    image_url = 'https://kmdevantagens.com.br/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FKMV_Logo_RGB_AzulTagline.0619db32.png&w=256&q=75'
    col2.title(' ')
    col1.image(image_url)
    col2.subheader('Assistente Vitual KMV')

    k = session_id

    msgs = StreamlitChatMessageHistory(key=k)

    llm = KMVAssist()

    for msg in msgs.messages:
        st.chat_message(msg.type).write(msg.content)

    if prompt := st.chat_input("Digite aqui sua pergunta sobre a KMV"):
        st.chat_message("human").write(prompt)
        chain = llm.llm(prompt)

        chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs, 
        input_messages_key="question",
        history_messages_key="history",
    )

        config = {"configurable": {"session_id": "any"}}
        response = chain_with_history.invoke({"question": prompt}, config)
        #with st.chat_message("ai").write(response.content)
        with st.chat_message("ai"):
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner("Pensando ⌛ ..."):
                resposta = response.content
                full_response_split = resposta.split()

            response_partial = ""

            for palavra in full_response_split:
                response_partial += palavra + " "
                message_placeholder.write(response_partial + "▌")
                tempo = random.uniform(0.05, 0.2)
                sleep(tempo)
        
        message_placeholder.write(resposta)


