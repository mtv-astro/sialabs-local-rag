# Local Setup

## Pré-requisitos

- Git
- Python 3.12+
- uv
- Node.js 22+
- Docker opcional
- Ollama opcional

## Backend

```powershell
cd backend
uv sync --dev
uv run uvicorn sialabs_local_rag.main:app --reload --host 0.0.0.0 --port 8000
```

## Frontend

```powershell
cd frontend
npm ci
npm run dev
```

## Docker

```powershell
copy .env.example .env
docker compose up --build
```

Com serviço Ollama no Compose:

```powershell
docker compose --profile llm up --build
```

## Teste manual rápido

1. Abra `http://localhost:5173`.
2. Clique em `Indexar texto` usando o documento de demonstração.
3. Pergunte: `Quais competências técnicas este projeto demonstra?`.
4. Verifique resposta e fontes recuperadas.

## Reset local

```powershell
Remove-Item -Recurse -Force .\data
```

O banco será recriado automaticamente pelo backend.
