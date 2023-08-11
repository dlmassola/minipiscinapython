#!/bin/sh

# Caminho para o executável do Python 3
PYTHON_PATH="/usr/bin/python3"

# Diretório para a criação do ambiente virtual
DIR="day06_env/"

# Criação do ambiente virtual usando o módulo 'venv' do Python
$PYTHON_PATH -m venv $DIR

. $DIR/bin/activate
# Verifica a versão do 'pip' instalado
pip --version

# Instalação de pacotes a partir do arquivo 'requirements.txt'
pip install --force-reinstall -r requirements.txt

echo "Ambiente virtual criado com sucesso!"