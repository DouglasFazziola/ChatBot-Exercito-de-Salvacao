import streamlit as st
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
from time import sleep
from langchain_core.runnables.history import RunnableWithMessageHistory
from llm import ExercitodeSalvacaoAssistant
import streamlit as st
import random
from streamlit.runtime.scriptrunner import get_script_run_ctx


def main():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = random.randint(1, 1000000)

    session_id = st.session_state["session_id"]

    try:
        st.set_page_config(
            page_title="Assistente Virtual Exército de Salvação",
            page_icon="https://static.wixstatic.com/media/5e1ee4_e7455edc66c74522937933a9df253402~mv2.png/v1/fill/w_120,h_134,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Novo%20Escudo%20-%20%C3%8Dcone%20Wix.png",
            initial_sidebar_state="collapsed",
            layout="centered",
    )
    except:
        st.experimental_rerun()

    col1,col2 = st.columns([3,8])
    image_url = 'https://static.wixstatic.com/media/5e1ee4_e7455edc66c74522937933a9df253402~mv2.png/v1/fill/w_120,h_134,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Novo%20Escudo%20-%20%C3%8Dcone%20Wix.png'
    col2.title('Assistente Virtual Exército de Salvação')
    col1.image(image_url)
    col2.subheader('')

    k = session_id

    msgs = StreamlitChatMessageHistory(key=k)

    llm = ExercitodeSalvacaoAssistant()

    for msg in msgs.messages:
        st.chat_message(msg.type).write(msg.content)

    if prompt := st.chat_input("Digite aqui sua pergunta sobre o Exérito de Salvação"):
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


