#!/bin/sh

CONTAINER_NAME="postgres-djangotraining"
POSTGRES_USER="djangouser"
POSTGRES_PASSWORD="secret"
POSTGRES_DB="djangotraining"

docker network create d06-network

docker run -d \
  --name "$CONTAINER_NAME" \
  --network d06-network \
  -e POSTGRES_USER="$POSTGRES_USER" \
  -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
  -e POSTGRES_DB="$POSTGRES_DB" \
  -p 5433:5432\
  postgres:latest

echo "PostgreSQL container '$CONTAINER_NAME' criado."

docker run -d \
  --name adminer-container \
  --network d06-network \
  -p 8080:8080 \
  adminer

echo "Adminer container 'adminer-container' criado."
echo "Acesse o Adminer em http://localhost:8080"

echo "Para acessar o banco de dados, utilize as seguintes credenciais:"
echo "Sistema: PostgreSQL"
echo "Servidor: postgres-djangotraining"
echo "Usuário: $POSTGRES_USER"
echo "Senha: $POSTGRES_PASSWORD"
echo "Banco de dados: $POSTGRES_DB"