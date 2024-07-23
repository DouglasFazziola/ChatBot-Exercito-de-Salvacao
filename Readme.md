# Chatbot - Exército de Salvação
**Versão:** 1.0

## Descrição do Projeto
Este projeto consiste em um chatbot que fornece informações sobre o Exército de Salvação, utilizando informações extraídas do site oficial do Exército de Salvação no Brasil (https://www.exercitodesalvacao.org.br/). O chatbot é alimentado por um modelo de linguagem da OpenAI, e foi desenvolvido utilizando o EdenAI através do framework LangChain para facilitar a integração e gerenciamento dos serviços de IA.

## Objetivo
O objetivo deste chatbot é facilitar o acesso a informações relevantes sobre o Exército de Salvação de forma rápida e eficiente através de uma interface de conversa amigável.

## Requisitos do Sistema
- Python 3.8 ou superior
- Pacotes listados em `requirements.txt`

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/DouglasFazziola/ChatBot-Exercito-de-Salvacao.git
   cd ChatBot-Exercito-de-Salvacao
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
Após iniciar o aplicativo, utilize a interface para fazer perguntas sobre o Exército de Salvação, como:
- "Qual é o Objetivo do Exército de Salvação?"
- "Quem fundou e quando foi fundado o Exército de Salvação?"
- "Quais são os projetos do Exército de Salvação no Brasil?"

## Funcionalidades
- **Respostas Automatizadas**: O chatbot responde a perguntas utilizando informações do site do Exército de Salvação.
- **Interface Amigável**: Interface de usuário desenvolvida com Streamlit para facilitar a interação.

## Estrutura do Projeto
 ```plaintext
 ├── app.py                # Arquivo responsável por iniciar a aplicação
 ├── collect.ipynb         # Notebooks Jupyter contendo o processo de web scraping, vetorização e embedding dos dados
 ├── llm.py                # Arquivo com as configurações e parâmetros para o modelo de linguagem (LLM)
 ├── ui.py                 # Arquivo que define e configura a interface do usuário
 ├── requirements.txt      # Arquivo que lista todas as dependências necessárias para executar o projeto
 ├── .gitignore            # Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git
 └── README.md             # Este arquivo README, que fornece uma visão geral do projeto e instruções de uso
 ```

## Contribuição
Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para discutir melhorias e sugestões.
