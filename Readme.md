# Chatbot - KMV
**Version:** 1.0

## Descrição do Projeto
Este projeto consiste em um chatbot que fornece informações sobre a KMV, uma empresa de vantagens e benefícios, utilizando informações extraídas do site oficial da KMV (https://kmdevantagens.com.br/). O chatbot é alimentado por um modelo de linguagem da OpenAI.

## Objetivo
O objetivo deste chatbot é facilitar o acesso a informações relevantes sobre a KMV de forma rápida e eficiente através de uma interface de conversa amigável.

## Requisitos do Sistema
- Python 3.8 ou superior
- Pacotes listados em `requirements.txt`

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/DouglasFazziola/LLM---KMV.git
   cd LLM---KMV
   ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Execução do App
Para iniciar o aplicativo, execute o seguinte comando:
    ```bash
    streamlit run app.py
    ```

## Como Usar
Após iniciar o aplicativo, utilize a interface para fazer perguntas sobre a KMV, como:
- "O que é a KMV?"
- "Quais são os benefícios oferecidos pela KMV?"

## Funcionalidades
- **Respostas Automatizadas**: O chatbot responde a perguntas utilizando informações do site da KMV.
- **Interface Amigável**: Interface de usuário desenvolvida com Streamlit para facilitar a interação.

## Estrutura do Projeto
    ```plaintext
    ├── app.py                # Arquivo principal do aplicativo, responsável por iniciar e configurar a aplicação
    ├── collect.ipynb         # Notebooks Jupyter contendo o processo de web scraping, vetorização e embedding dos dados
    ├── llm.py                # Arquivo com as configurações e parâmetros para o modelo de linguagem (LLM)
    ├── ui.py                 # Arquivo que define e configura a interface do usuário
    ├── requirements.txt      # Arquivo que lista todas as dependências necessárias para executar o projeto
    ├── .gitignore            # Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git
    ├── .streamlit            # arquivo contendo os ajustes cores específicas do fundo da interface do Streamlit
    └── README.md             # Este arquivo README, que fornece uma visão geral do projeto e instruções de uso
    ```

## Contribuição
Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para discutir melhorias e sugestões.