PYTHON_PATH="/usr/bin/python3"

DIRETORIO_AMBIENTE="django_venv"

 # dentro do ex04, ira criar a pasta django_venv
$PYTHON_PATH -m venv $DIRETORIO_AMBIENTE

source $DIRETORIO_AMBIENTE/bin/activate

python3 -m pip install --force-reinstall -r requirement.txt

echo "requirement.txt instalada com sucesso"
