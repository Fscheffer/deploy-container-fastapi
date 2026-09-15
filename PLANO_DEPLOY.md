# Plano de Deploy

## Recursos Azure já definidos

- Resource Group: `rg-python-aula`
- Região: `Canada Central`
- Azure Container Registry: `acrpythonfastapi915`
- Login server: `acrpythonfastapi915.azurecr.io`
- PostgreSQL Flexible Server: `pg-deploy-fastapi-2026fg`
- Azure Web App: `app-fastapi-deploy-2026yh`
- Container port: `8000`

## Sequência

1. GitHub recebe o código.
2. GitHub Actions executa os testes.
3. Se os testes passarem na branch `main`, a imagem Docker é criada.
4. A imagem é enviada ao ACR como `fastapi-deploy:latest` e também com o SHA do commit.
5. O Azure Web App será configurado para consumir `fastapi-deploy:latest`.
6. A variável `DATABASE_URL` será configurada no Web App para conectar ao PostgreSQL.
7. A aplicação será validada pelos endpoints `/health` e `/docs`.

## Observação

As credenciais do ACR e do PostgreSQL não devem ser versionadas no repositório.
