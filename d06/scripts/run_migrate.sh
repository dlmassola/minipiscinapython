#!/bin/sh
DIR="day06_env"

# Caminho para o diretório onde está localizado o arquivo manage.py
PROJECT_DIR="d06"

. $DIR/bin/activate

# Execute o comando makemigrations para criar a migração
python3 $PROJECT_DIR/manage.py makemigrations

# Execute o comando migrate para aplicar a migração ao banco de dados
python3 $PROJECT_DIR/manage.py migrate 
