DIRETORIO_AMBIENTE="django_venv"

python3 -m venv $DIRETORIO_AMBIENTE

. $DIRETORIO_AMBIENTE/bin/activate

python3 -m pip install --force-reinstall -r requirement.txt
