import streamlit as st
from langchain.vectorstores import Chroma
from langchain_community.chat_models.edenai import ChatEdenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.embeddings.edenai import EdenAiEmbeddings
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)
import os, random
from time import sleep


from dotenv import load_dotenv
load_dotenv()

class KMVAssist:

    def __init__(self):
        self.api_key = os.getenv("EDENAI_API_KEY")
        

    def llm(self, prompt):

        chat = ChatEdenAI(edenai_api_key=self.api_key, provider="openai", temperature=0.0, max_tokens=2500, verbose=True)

        persist_directory = 'kmv_embedding'
        colletion_vector_coopercitrus = 'kmv_collection'
        embeddings = EdenAiEmbeddings(provider="openai", edenai_api_key=self.api_key)

        def chamar_contexto(pergunta: str) -> str:
                contexto = db.similarity_search(query = pergunta, k=5)
                contexto = "---".join([doc.page_content for doc in contexto]).replace('\n','  ')
                return contexto

        db = Chroma(collection_name=colletion_vector_coopercitrus, 
                        persist_directory=persist_directory, 
                        embedding_function=embeddings)

        m = "Voce é um chatbot que ajuda a dar informações sobre a KMV. Não responda perguntas que não tenha relação com a KMV. Se alguem fizer uma pergunta que não tenha nada a ver com a KMV, diga de um jeito comico e bem humorado que não sabe a resposta. Se alguem perguntar quem desenvolveu você, diga que foi um grande desenvolvedor chamado Douglas Campelo Fazziola, mas apenas se perguntar"

        contexto = chamar_contexto(prompt)

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", f'{m}\n contexto: {contexto}'),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{question}"),
            ]
        )

        chain = prompt | chat

        return chain

