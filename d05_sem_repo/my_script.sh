PYTHON_PATH="/usr/bin/python3"

DIRETORIO_AMBIENTE="django_venv"

# python3 -m pip --version

export PATH=$PATH:/nfs/homes/dluiz-ma/.local/bin

$PATH

# python3 -m pip install --force-reinstall -r requirements.txt

$PYTHON_PATH -m venv $DIRETORIO_AMBIENTE

. $DIRETORIO_AMBIENTE/bin/activate

# django-admin startproject d05 .

django-admin startapp ex00
django-admin startapp ex01
django-admin startapp ex02
django-admin startapp ex03
django-admin startapp ex04
django-admin startapp ex05
django-admin startapp ex06
django-admin startapp ex07
django-admin startapp ex08
django-admin startapp ex09
django-admin startapp ex10
