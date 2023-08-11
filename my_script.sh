DIRETORIO_AMBIENTE="django_venv"

python3 -m venv $DIRETORIO_AMBIENTE

. $DIRETORIO_AMBIENTE/bin/activate

python3 -m pip install --force-reinstall -r requirements.txt

python3 manage.py runserver

# Criação do projeto
# django-admin startproject d06

# Criação da aplicação
# cd d06

# django-admin startapp ex00
# django-admin startapp ex01
# django-admin startapp ex02
# django-admin startapp ex03
# django-admin startapp ex04
# django-admin startapp ex05
# django-admin startapp ex06
