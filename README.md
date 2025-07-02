# library-db-postgresql

Repositório para acesso a banco de dados PostgreSQL utilizando SQLAlchemy.

## Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Como executar com Docker

### Build da imagem

```bash
docker build -t meu-postgres .
```

### Subindo o container

```bash
docker run --name bd \
    -e POSTGRES_DB=bd \
    -e POSTGRES_USER=usuario \
    -e POSTGRES_PASSWORD=senha123 \
    -p 5432:5432 \
    -d meu-postgres
```

## Como executar com Docker Compose

```bash
docker compose up --build -d
```

## Conexão com o banco

- **Host:** localhost
- **Porta:** 5432
- **Usuário:** usuario
- **Senha:** senha123
- **Banco:** bd

## Observações

- Certifique-se de que a porta 5432 está disponível.
- Altere as variáveis de ambiente conforme necessário para seu ambiente de desenvolvimento.
- Para parar e remover os containers:

```bash
docker compose down
```