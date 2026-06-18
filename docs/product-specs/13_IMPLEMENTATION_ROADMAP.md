# Implementation Roadmap

## 1. Estratégia geral

Produzir o projeto em fatias pequenas, cada uma com valor técnico visível. O objetivo é que o histórico do GitHub conte uma história profissional.

## 2. Fase 0 — Especificação e repositório

### Objetivo

Criar base documental e estrutural.

### Entregas

- README inicial.
- PRD e specs.
- Backlog.
- Templates de issue/PR.

### PRs esperados

- `docs(product): add PRD and project specs`
- `chore(repo): scaffold monorepo structure`

## 3. Fase 1 — Qualidade e fundação técnica

### Objetivo

Criar backend/frontend mínimos e validação automática.

### Entregas

- FastAPI app shell.
- Vite app shell.
- CI.
- `.env.example`.

### PRs esperados

- `ci(repo): add backend and frontend validation workflow`
- `feat(api): add FastAPI app shell and health endpoints`
- `feat(frontend): add app shell`

## 4. Fase 2 — Dados e documentos

### Objetivo

Permitir upload, persistência e extração de texto.

### Entregas

- SQLite schema.
- Migrations.
- Upload validation.
- Parsers `.txt`, `.md`, `.pdf`.

### PRs esperados

- `feat(db): add initial SQLite schema and migrations`
- `feat(documents): add document upload and validation`
- `feat(documents): add text extraction for txt markdown and pdf`

## 5. Fase 3 — Pipeline RAG

### Objetivo

Transformar documentos em base semântica.

### Entregas

- Chunking.
- Embeddings.
- Vector search.
- Retrieval service.

### PRs esperados

- `feat(rag): add chunking service`
- `feat(ai): add local embedding generation`
- `feat(rag): add semantic retrieval service`

## 6. Fase 4 — Chat fundamentado

### Objetivo

Responder perguntas com base nos documentos.

### Entregas

- Ollama chat client.
- Prompt seguro.
- Respostas com fontes.
- Traces.

### PRs esperados

- `feat(chat): add grounded answer generation with sources`
- `feat(rag): add retrieval traces`
- `security(ai): add prompt injection guardrails and tests`

## 7. Fase 5 — Frontend funcional

### Objetivo

Criar experiência de uso demonstrável.

### Entregas

- Dashboard/status.
- Biblioteca/upload.
- Chat.
- Painel de fontes.

### PRs esperados

- `feat(frontend): add app shell and status dashboard`
- `feat(frontend): add document library and upload UI`
- `feat(frontend): add chat UI with source panel`

## 8. Fase 6 — Operação e release

### Objetivo

Deixar projeto rodável, apresentável e seguro para portfólio.

### Entregas

- Docker Compose.
- Demo docs.
- Screenshots.
- Release notes.
- Tag v0.1.

### PRs esperados

- `build(docker): add local Docker Compose setup`
- `docs(recruiting): add case study and demo guide`
- `chore(release): prepare v0.1 portfolio release`

## 9. Definição de pronto por fase

Cada fase está pronta quando:

- PRs foram mergeados com CI verde.
- README/docs foram atualizados.
- Validações locais foram rodadas.
- Não há arquivos fora do escopo.
- A main está limpa.

## 10. Prioridade de entrega

Ordem de prioridade:

1. App rodando.
2. Upload e ingestão.
3. Retrieval.
4. Chat com fontes.
5. UI polida.
6. Segurança e testes.
7. Demo e docs finais.

## 11. O que cortar se o prazo apertar

Cortar primeiro:

- Playwright.
- PDF avançado.
- Busca híbrida.
- Configurações editáveis pela UI.
- Docker para frontend separado.
- Traces detalhados demais.

Não cortar:

- README.
- `.env.example`.
- CI básico.
- Testes do core RAG.
- Resposta de insuficiência.
- Fontes na resposta.
