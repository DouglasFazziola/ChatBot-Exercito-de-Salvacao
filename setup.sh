#!/bin/bash

# Atualizar pip
pip install --upgrade pip

# Instalar dependências do sistema
if [ -f "packages.txt" ]; then
    xargs -a packages.txt sudo apt-get install -y
fi

# Instalar dependências Python
pip install -r requirements.txt