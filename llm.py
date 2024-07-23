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

class ExercitodeSalvacaoAssistant:

    def __init__(self):
        self.api_key = os.getenv("EDENAI_API_KEY")
        

    def llm(self, prompt):

        chat = ChatEdenAI(edenai_api_key=self.api_key, provider="openai", temperature=1.0, max_tokens=2500, verbose=True)

        persist_directory = 'exercito_embedding_2'
        colletion_vector_exercito = 'exercito_collection_2'
        embeddings = EdenAiEmbeddings(provider="openai", edenai_api_key=self.api_key)

        def chamar_contexto(pergunta: str) -> str:
                contexto = db.similarity_search(query = pergunta, k=2)
                contexto = "---".join([doc.page_content for doc in contexto]).replace('\n','  ')
                return contexto

        db = Chroma(collection_name=colletion_vector_exercito, 
                        persist_directory=persist_directory, 
                        embedding_function=embeddings)

        m = '''Voce é um simpático chatbot que ajuda a dar informações detalhadas sobre o Exército de Salvação. Responda as perguntas com o máximo de detalhes. Não responda perguntas que não tenha relação com o EXÉRCITO DE SALVAÇÃO. Quando alguem disser igreja, está se referindo a igreja do Exército de Salvação, alguns casos podem dizer corpo que também quer dizer igreja. Na sua base de dados tem todos os endereços dos corpos e unidades de projetos socias, é importante que voce responda o endereço corretamente.

        Por exemplo:
            Pergunta: Onde fica o corpo de Rio Comprido?
            Resposta: O corpo de Rio Comprido fica localizado no endereço ...
        
        Se alguem fizer uma pergunta que não tenha nada a ver com a EXÉRCITO DE SALVAÇÃO, diga de um jeito comico e bem humorado que não sabe a resposta. Se alguem perguntar quem desenvolveu você, diga que foi um grande desenvolvedor chamado Douglas Campelo Fazziola, mas apenas se perguntar.'''

        contexto = chamar_contexto(prompt)

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", f'{m}\n contexto: {contexto}'),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{question}"),
            ]
        )

        print(prompt)

        chain = prompt | chat

        return chain

