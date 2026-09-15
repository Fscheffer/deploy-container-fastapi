# Deploy Container FastAPI

Projeto de demonstração de uma API FastAPI empacotada em Docker e publicada em um Azure Container Registry (ACR), com automação pelo GitHub Actions.

## Arquitetura

GitHub → GitHub Actions → testes → Docker build → Azure Container Registry → Azure Web App → FastAPI → PostgreSQL

## Endpoints

- `GET /` — verifica se a API está funcionando.
- `GET /health` — health check.
- `GET /api/products` — lista produtos.
- `GET /api/products/{id}` — consulta um produto.
- `POST /api/products` — cria produto.
- `PUT /api/products/{id}` — atualiza produto.
- `DELETE /api/products/{id}` — exclui produto.
- `/docs` — documentação Swagger.

## Rodar localmente

Com Docker Compose:

```bash
docker compose up --build
```

A API ficará em `http://localhost:8000`.

## Banco no Azure

No Azure Web App, configure a variável de ambiente `DATABASE_URL` com a string de conexão do PostgreSQL Flexible Server.

Não coloque senha do banco no GitHub, no código ou no README.

## GitHub Actions

O workflow executa os testes e, na branch `main`, cria a imagem Docker e publica duas tags no ACR:

- `fastapi-deploy:latest`
- `fastapi-deploy:<SHA do commit>`

Secrets necessários:

- `ACR_LOGIN_SERVER`
- `ACR_USERNAME`
- `ACR_PASSWORD`
