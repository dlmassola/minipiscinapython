#!/bin/sh

echo "================================Criando ambiente virtual================================"

./scripts/create_venv.sh

clear

echo "================================Criando infra do projeto================================"

./scripts/docker_container.sh

clear

echo "================================Rodar Migrações================================"

./scripts/run_migrate.sh

clear

echo "================================Executando projeto================================"

./scripts/run_project.sh