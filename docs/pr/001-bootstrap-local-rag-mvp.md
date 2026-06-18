Closes #1.

## Summary

- Bootstrap the monorepo with FastAPI backend, React/Vite/TypeScript frontend, Docker Compose and GitHub Actions.
- Implements a local-first RAG MVP with text/Markdown ingestion, chunking, deterministic CI embeddings, SQLite storage, similarity search and chat with sources.
- Adds optional Ollama providers for local chat and embeddings, while keeping mock/hash mode for validation without external models.
- Includes architecture, API, local setup, security, testing, GitHub workflow and recruiter evidence documentation.

## Validation

- [x] `cd backend && uv run ruff check . --fix`
- [x] `cd backend && uv run ruff check .`
- [x] `cd backend && uv run pytest`
- [x] `cd backend && uv run mypy src`
- [x] `cd frontend && npm install`
- [x] `cd frontend && npm run typecheck`
- [x] `cd frontend && npm run build`
- [x] `docker compose config`
- [x] `git status --short`
- [x] `git diff --cached --stat`

## Review checklist

- [x] PR scope matches the issue.
- [x] No real `.env`, tokens, keys or sensitive data committed.
- [x] CI is green.
- [x] README documents demo/hash mode and Ollama mode.
- [x] Git history is clean enough for portfolio presentation.