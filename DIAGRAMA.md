# Diagrama da solução

```text
┌───────────────┐
│    GitHub     │
│ código + CI   │
└───────┬───────┘
        │ push
        ▼
┌──────────────────────┐
│   GitHub Actions     │
│ testes + Docker      │
└──────────┬───────────┘
           │ push image
           ▼
┌──────────────────────┐
│ Azure Container      │
│ Registry             │
│ fastapi-deploy:latest│
└──────────┬───────────┘
           │ pull
           ▼
┌──────────────────────┐
│ Azure Web App        │
│ FastAPI / port 8000  │
└──────────┬───────────┘
           │ DATABASE_URL
           ▼
┌──────────────────────┐
│ PostgreSQL Flexible  │
│ Server               │
└──────────────────────┘
```
