#!/bin/sh

VENV_NAME="day06_env"

# Ativar o ambiente virtual                                                     
. $VENV_NAME/bin/activate

# Navegar para o diretório do projeto Django                                    
cd d06
# Iniciar o projeto Django (substitua 'projectname' pelo nome do seu projeto)   
python3 manage.py runserver
