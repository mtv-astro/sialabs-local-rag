# SIALabs Local RAG

Local-first RAG assistant for private documents using Gemma 4 via Ollama.

## Overview

SIALabs Local RAG is a portfolio project that demonstrates full stack development, local AI, RAG, document ingestion, semantic search, grounded answers with sources, Docker, tests and CI.

## Features

- Local document upload
- `.txt`, `.md`, `.pdf` support
- Chunking and embeddings
- Local semantic search
- Gemma 4 chat via Ollama
- Answers with sources
- RAG traces
- Local SQLite database
- Docker Compose
- GitHub Actions

## Tech Stack

- React + Vite + TypeScript
- FastAPI + Python
- SQLite
- Ollama
- Gemma 4
- EmbeddingGemma
- Docker
- GitHub Actions

## Getting Started

```powershell
ollama pull gemma4:e4b
ollama pull embeddinggemma
```

Then configure `.env` from `.env.example` and start the app.

## Validation

```powershell
cd backend
uv run ruff check .
uv run pytest
uv run mypy src

cd ../frontend
npm run lint
npm run typecheck
npm run build
```

## Security and Privacy

The main flow runs locally. Uploaded documents, embeddings and traces are stored in local data files ignored by Git.

## Portfolio Evidence

This project demonstrates:

- full stack architecture;
- local AI integration;
- RAG pipeline design;
- document processing;
- database modeling;
- API design;
- UI/UX states;
- security awareness;
- testing and CI;
- GitHub delivery workflow.
