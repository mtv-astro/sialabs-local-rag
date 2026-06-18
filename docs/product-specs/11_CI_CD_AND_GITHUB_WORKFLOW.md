# CI/CD and GitHub Workflow

## 1. Objetivo

Transformar o desenvolvimento do projeto em evidência pública de maturidade profissional.

A implementação deve ser incremental, rastreável e validada. Cada entrega deve ter issue, branch, commit, PR, validação e CI.

## 2. Fluxo padrão

```text
Issue -> Branch -> Implementação local -> Validação local -> Commit -> Push -> PR -> CI -> Revisão -> Merge -> Sync local
```

## 3. Convenções

Usar Conventional Commits para issue, branch, commit e PR.

Formato:

```text
type(scope): short description
```

Tipos:

- `feat`
- `fix`
- `docs`
- `test`
- `ci`
- `build`
- `refactor`
- `chore`

Escopos sugeridos:

- `repo`
- `api`
- `frontend`
- `rag`
- `ai`
- `db`
- `docs`
- `security`
- `docker`
- `ci`
- `demo`

## 4. Branches

Exemplos:

```text
docs/project-specs
chore/repo-scaffold
feat/api-health
feat/rag-ingestion
feat/ai-ollama-client
feat/frontend-chat
security/prompt-injection-guards
ci/project-validation
```

## 5. Commits

Exemplos:

```text
docs(product): add PRD and architecture specs
chore(repo): scaffold backend and frontend workspaces
feat(api): add health and model status endpoints
feat(rag): add document chunking service
test(rag): cover prompt injection document case
ci(repo): add backend and frontend validation workflow
```

## 6. PR template

Usar `docs/templates/PULL_REQUEST_TEMPLATE.md`.

Cada PR deve conter:

- issue relacionada;
- resumo;
- validação;
- riscos;
- screenshots quando houver UI;
- observações de escopo.

## 7. CI mínimo

GitHub Actions deve rodar:

### Backend

- instalar dependências com `uv`;
- `ruff check`;
- `pytest`;
- `mypy`.

### Frontend

- instalar dependências;
- lint;
- typecheck;
- build.

### Segurança simples

- checar ausência de `.env` real;
- garantir que `data/` e `uploads/` estão ignorados.

## 8. Comandos locais por PR

Backend:

```powershell
cd backend
uv run ruff check . --fix
uv run ruff check .
uv run pytest
uv run mypy src
```

Frontend:

```powershell
cd frontend
npm run lint
npm run typecheck
npm run build
```

Raiz:

```powershell
git status --short
git diff --stat
```

## 9. Regras antes do commit

- Não commitar sem rodar validações possíveis.
- Conferir `git diff --stat`.
- Conferir arquivos novos no stage.
- Não incluir `.env`, banco local, uploads ou logs.
- Commits devem ser pequenos e claros.

## 10. Regras antes do merge

- CI verde.
- PR referencia issue.
- Diff revisado.
- Escopo fechado.
- Sem arquivos sensíveis.
- Sem mudanças acidentais.

## 11. Milestones sugeridos

### M0 — Project definition

- docs iniciais;
- README base;
- backlog.

### M1 — Repo foundation

- monorepo;
- backend/frontend scaffold;
- CI básico.

### M2 — Backend core

- health;
- config;
- database;
- documents.

### M3 — RAG pipeline

- parsing;
- chunking;
- embeddings;
- retrieval.

### M4 — Chat

- geração;
- fontes;
- traces.

### M5 — Frontend

- dashboard;
- biblioteca;
- chat;
- fontes.

### M6 — Hardening and release

- segurança;
- testes;
- Docker;
- demo;
- docs finais.

## 12. Estratégia de PRs pequenos

Evitar um PR gigante chamado “implement app”. A entrega deve parecer profissional.

Sequência recomendada:

1. `docs(product): add PRD and execution specs`
2. `chore(repo): scaffold project structure`
3. `ci(repo): add validation workflow`
4. `feat(api): add health and settings`
5. `feat(db): add initial schema and migrations`
6. `feat(rag): add document ingestion pipeline`
7. `feat(ai): add ollama adapters`
8. `feat(rag): add semantic retrieval`
9. `feat(chat): add grounded answer generation`
10. `feat(frontend): add dashboard and document library`
11. `feat(frontend): add chat with sources`
12. `security(ai): add prompt injection tests and guardrails`
13. `build(docker): add local compose setup`
14. `docs(demo): add recruiter demo guide`

## 13. Evidência final

Ao final, o GitHub deve mostrar:

- issues bem escritas;
- PRs com validação;
- commits padronizados;
- CI passando;
- documentação robusta;
- main limpa.
