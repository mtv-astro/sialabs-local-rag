# feat(app): bootstrap local RAG MVP

## Problem

O projeto precisa sair da fase de PRD para uma primeira entrega executável, revisável e demonstrável em portfólio. A base inicial deve provar que o repositório tem arquitetura full stack, API funcional, UI mínima, fluxo RAG testável, documentação e CI.

## Scope

- Criar estrutura de monorepo com `backend/`, `frontend/`, `docs/`, `issues/` e `.github/`.
- Implementar backend FastAPI com endpoints de health, configuração pública, ingestão de documentos, upload simples, listagem, exclusão e chat RAG.
- Implementar chunking com overlap, embeddings locais determinísticos para CI e integração opcional com Ollama.
- Persistir documentos, chunks, embeddings e registros de chat em SQLite.
- Implementar frontend React/Vite/TypeScript para ingestão, upload, listagem, chat e visualização de fontes.
- Adicionar Dockerfile do backend, Dockerfile do frontend e `docker-compose.yml`.
- Adicionar GitHub Actions para lint, testes, typecheck e build.
- Documentar arquitetura, setup local, IA local, API, segurança, testes e evidências para recrutamento.

## Out of scope

- Autenticação e multiusuário.
- Deploy público.
- Parser de PDF.
- Banco vetorial externo.
- Observabilidade avançada.
- Integração com Supabase.
- Streaming de respostas.

## Acceptance criteria

- `cd backend && uv run ruff check .`
- `cd backend && uv run pytest`
- `cd backend && uv run mypy src`
- `cd frontend && npm run typecheck`
- `cd frontend && npm run build`
- `docker compose config` executa sem erro.
- `README.md` explica execução com mock/hash e com Ollama.
- `.env.example` existe e não contém segredos reais.
- O PR usa branch `feat/bootstrap-local-rag`.
- O PR referencia esta issue.
- CI deve ficar verde antes de merge.

## Suggested branch

`feat/bootstrap-local-rag`

## Suggested commit

`feat(app): bootstrap local RAG MVP`
