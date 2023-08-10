python3 -m pip install --force-reinstall -r requirements.txt

# configuração e instalação do DJANGO
DIRETORIO_AMBIENTE="django_venv"

python3 -m venv $DIRETORIO_AMBIENTE

. $DIRETORIO_AMBIENTE/bin/activate

# Criação do projeto
django-admin startproject d04 .

# Criação da aplicação
django-admin startapp ex00

django-admin startapp ex01

django-admin startapp ex02

django-admin startapp ex03