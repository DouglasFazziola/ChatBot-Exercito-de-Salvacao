#!/bin/bash

# Nome do projeto
echo "Chatbot - KMV"
echo "Version: 1.0"

# Descrição do projeto
echo "Este projeto consiste em um chatbot que fornece informações sobre a KMV, utilizando dados extraídos do site oficial https://kmdevantagens.com.br/."

# Objetivo
echo "Facilitar o acesso a informações sobre a KMV de forma rápida e eficiente através de uma interface de chatbot."

# Requisitos do Sistema
echo "Requisitos do Sistema:"
echo "- Python 3.8 ou superior"
echo "- Pacotes listados em requirements.txt"

# Clonar o repositório
echo "Clonando o repositório..."
git clone https://github.com/DouglasFazziola/LLM---KMV.git
cd LLM---KMV

# Criar ambiente virtual e ativá-lo
echo "Criando ambiente virtual..."
python -m venv venv
echo "Ativando ambiente virtual..."
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instalar as dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Executar o app
echo "Para iniciar o aplicativo, execute o seguinte comando:"
echo "streamlit run app.py"

# Como usar
echo "Após iniciar o aplicativo, utilize a interface para fazer perguntas sobre a KMV, como:"
echo "- 'O que é a KMV?'"
echo "- 'Quais são os benefícios oferecidos pela KMV?'"

# Funcionalidades
echo "Funcionalidades:"
echo "- Respostas Automatizadas: O chatbot responde a perguntas utilizando informações do site da KMV."
echo "- Interface Amigável: Interface de usuário desenvolvida com Streamlit para facilitar a interação."
echo "- Atualizações Dinâmicas: Informações atualizadas regularmente através de web scraping."

# Estrutura do Projeto
echo "Estrutura do Projeto:"
echo "├── app.py                # Arquivo principal do aplicativo"
echo "├── requirements.txt      # Dependências do projeto"
echo "├── README.md             # Este arquivo README"
echo "└── data/"
echo "    └── scraping.py       # Script de web scraping para obter informações da KMV"

# Contribuição
echo "Contribuição:"
echo "Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para discutir melhorias e sugestões."

# Licença
echo "Licença:"
echo "Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes."
