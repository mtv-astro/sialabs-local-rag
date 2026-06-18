# Backlog and Issue Specs

## Como usar

Cada item abaixo pode virar uma issue do GitHub. O título já segue Conventional Commits. O escopo foi pensado para PRs pequenos e avaliáveis.

---

## Issue 01 — `docs(product): add PRD and project specs`

### Problem

O projeto precisa de especificação clara antes da implementação para orientar escopo, arquitetura, riscos e evidências de portfólio.

### Scope

- Adicionar PRD.
- Adicionar Product Spec.
- Adicionar Technical Spec.
- Adicionar Architecture Spec.
- Adicionar Backlog inicial.
- Adicionar README inicial.

### Out of scope

- Implementar código da aplicação.
- Criar UI real.

### Acceptance criteria

- `docs/01_PRD.md` existe.
- `docs/04_ARCHITECTURE.md` existe.
- `docs/12_BACKLOG_ISSUES.md` existe.
- README explica objetivo e stack.

---

## Issue 02 — `chore(repo): scaffold monorepo structure`

### Problem

O repositório precisa de estrutura base para backend, frontend, docs e demo.

### Scope

- Criar pastas `backend/`, `frontend/`, `docs/`, `demo/`.
- Criar `.gitignore`.
- Criar `.env.example`.
- Criar README de setup.

### Out of scope

- Implementar funcionalidades.
- Configurar CI completo.

### Acceptance criteria

- Estrutura base criada.
- `.env.example` documenta variáveis iniciais.
- `.gitignore` ignora `.env`, `data/`, `uploads/`, caches e builds.

---

## Issue 03 — `ci(repo): add backend and frontend validation workflow`

### Problem

O projeto precisa validar PRs automaticamente.

### Scope

- Adicionar GitHub Actions.
- Backend: ruff, pytest, mypy.
- Frontend: lint, typecheck, build.
- Documentar validação no README.

### Out of scope

- Deploy automático.
- Testes e2e pesados.

### Acceptance criteria

- CI roda em pull request.
- CI falha se lint/test/typecheck falhar.
- README lista comandos equivalentes locais.

---

## Issue 04 — `feat(api): add FastAPI app shell and health endpoints`

### Problem

A aplicação precisa de backend base e endpoints de saúde.

### Scope

- Criar app FastAPI.
- Adicionar `GET /health`.
- Adicionar configuração com Pydantic Settings.
- Adicionar testes.

### Out of scope

- Banco de dados.
- Ollama real.

### Acceptance criteria

- `/health` retorna 200.
- Teste de health passa.
- Configuração lê `.env`.

---

## Issue 05 — `feat(ai): add Ollama model status client`

### Problem

O sistema precisa verificar se Ollama e modelos locais estão disponíveis.

### Scope

- Criar `OllamaClient`.
- Implementar status do serviço.
- Implementar listagem/verificação de modelos.
- Criar `GET /api/models/status`.
- Adicionar testes com mock.

### Out of scope

- Geração de resposta.
- Embeddings.

### Acceptance criteria

- Endpoint retorna status do Ollama.
- Erro de conexão vira 503.
- Modelo ausente gera mensagem acionável.

---

## Issue 06 — `feat(db): add initial SQLite schema and migrations`

### Problem

O projeto precisa persistir documentos, chunks, mensagens e traces.

### Scope

- Configurar SQLAlchemy.
- Configurar Alembic.
- Criar tabelas iniciais.
- Criar repositories básicos.
- Adicionar testes simples.

### Out of scope

- Busca vetorial completa.
- UI.

### Acceptance criteria

- Migration inicial criada.
- `alembic upgrade head` funciona.
- Teste cria e busca documento.

---

## Issue 07 — `feat(documents): add document upload and validation`

### Problem

O usuário precisa importar documentos suportados.

### Scope

- Endpoint `POST /api/documents`.
- Validação de extensão/tamanho.
- Sanitização de nome.
- Hash SHA-256.
- Deduplicação.
- Listagem `GET /api/documents`.

### Out of scope

- Parsing PDF completo.
- Embeddings.

### Acceptance criteria

- Upload `.txt` aceito.
- Extensão inválida recusada.
- Documento duplicado tratado.
- Testes cobrem sucesso e erro.

---

## Issue 08 — `feat(documents): add text extraction for txt markdown and pdf`

### Problem

O sistema precisa extrair texto dos arquivos importados.

### Scope

- Parser `.txt`.
- Parser `.md`.
- Parser `.pdf`.
- Tratamento de PDF sem texto.
- Testes com fixtures.

### Out of scope

- OCR.
- Imagens.

### Acceptance criteria

- Texto extraído de `.txt` e `.md`.
- PDF simples extraído.
- PDF sem texto retorna erro controlado.

---

## Issue 09 — `feat(rag): add chunking service`

### Problem

Documentos precisam ser quebrados em chunks recuperáveis.

### Scope

- Serviço de normalização.
- Chunking com overlap.
- Metadados de chunk.
- Testes unitários.

### Out of scope

- Embeddings.
- Retrieval.

### Acceptance criteria

- Chunks respeitam tamanho aproximado.
- Overlap funciona.
- Chunks vazios são descartados.
- Testes cobrem documento curto e longo.

---

## Issue 10 — `feat(ai): add local embedding generation`

### Problem

Chunks precisam de embeddings para busca semântica.

### Scope

- Criar `EmbeddingClient` protocol.
- Criar `OllamaEmbeddingClient`.
- Usar `/api/embed`.
- Persistir embeddings.
- Criar fake client para testes.

### Out of scope

- Chat generation.
- UI.

### Acceptance criteria

- Embeddings são gerados para chunks.
- Falha do Ollama vira status `failed`.
- Testes usam fake client.

---

## Issue 11 — `feat(rag): add semantic retrieval service`

### Problem

O sistema precisa recuperar chunks relevantes para uma pergunta.

### Scope

- Gerar embedding da query.
- Buscar top-k chunks.
- Calcular similaridade.
- Aplicar threshold.
- Retornar sources.

### Out of scope

- Geração com LLM.
- Re-ranking.

### Acceptance criteria

- Query retorna chunks relevantes em fixture.
- Query fora da base retorna lista vazia ou abaixo do threshold.
- Testes cobrem busca.

---

## Issue 12 — `feat(chat): add grounded answer generation with sources`

### Problem

O usuário precisa receber resposta baseada nos documentos.

### Scope

- Criar `ChatGenerationService`.
- Criar `OllamaChatClient`.
- Montar prompt com contexto.
- Exigir fontes.
- Retornar insuficiência sem contexto.
- Persistir mensagem.

### Out of scope

- Streaming.
- Multi-agent.

### Acceptance criteria

- Pergunta com contexto retorna resposta.
- Pergunta sem contexto retorna insuficiência.
- Resposta inclui sources.
- Testes com fake chat client.

---

## Issue 13 — `feat(rag): add retrieval traces`

### Problem

O projeto precisa mostrar transparência do pipeline RAG.

### Scope

- Criar tabela de traces.
- Registrar top-k, scores, modelos e tempos.
- Criar endpoint `GET /api/rag/traces/{id}`.
- Exibir trace resumido na resposta.

### Out of scope

- Dashboard avançado.

### Acceptance criteria

- Cada pergunta gera trace.
- Endpoint retorna trace.
- Testes cobrem persistência.

---

## Issue 14 — `feat(frontend): add app shell and status dashboard`

### Problem

Usuário precisa ver se o ambiente local está pronto.

### Scope

- Criar app shell.
- Criar dashboard.
- Consumir `/health` e `/api/models/status`.
- Exibir erros acionáveis.

### Out of scope

- Upload.
- Chat.

### Acceptance criteria

- Dashboard exibe status.
- Estado de erro visível.
- Build passa.

---

## Issue 15 — `feat(frontend): add document library and upload UI`

### Problem

Usuário precisa importar e gerenciar documentos pela UI.

### Scope

- Dropzone/upload.
- Lista de documentos.
- Status pills.
- Remoção com confirmação.

### Out of scope

- Chat.

### Acceptance criteria

- Upload funciona contra API.
- Lista atualiza.
- Arquivo inválido mostra erro.

---

## Issue 16 — `feat(frontend): add chat UI with source panel`

### Problem

Usuário precisa conversar com a base e conferir fontes.

### Scope

- Tela de chat.
- Histórico de mensagens.
- Envio de pergunta.
- Painel de fontes.
- Estados loading/error.

### Out of scope

- Streaming.
- Markdown avançado.

### Acceptance criteria

- Pergunta retorna resposta.
- Fontes aparecem.
- Sem documentos mostra orientação.

---

## Issue 17 — `security(ai): add prompt injection guardrails and tests`

### Problem

Documentos podem conter instruções maliciosas que tentam manipular o LLM.

### Scope

- Ajustar system prompt.
- Adicionar fixture com prompt injection.
- Testar comportamento esperado.
- Documentar risco.

### Out of scope

- Firewall ou segurança empresarial.

### Acceptance criteria

- Teste de prompt injection passa.
- README/docs explicam mitigação.

---

## Issue 18 — `build(docker): add local Docker Compose setup`

### Problem

O projeto precisa ser fácil de rodar localmente.

### Scope

- Dockerfile backend.
- Dockerfile frontend ou build dev.
- Docker Compose.
- Documentar uso com Ollama local.
- Healthchecks.

### Out of scope

- Deploy cloud.

### Acceptance criteria

- `docker compose up` sobe app.
- README explica pré-requisitos de modelos.
- `.env.example` atualizado.

---

## Issue 19 — `docs(recruiting): add case study and demo guide`

### Problem

O projeto precisa ser fácil de apresentar para recrutamento.

### Scope

- Criar guia de demo.
- Criar matriz de competências.
- Criar seção de trade-offs no README.
- Criar screenshots ou instruções para adicionar screenshots.

### Out of scope

- Vídeo final.

### Acceptance criteria

- Recrutador entende o valor em poucos minutos.
- README lista competências demonstradas.

---

## Issue 20 — `chore(release): prepare v0.1 portfolio release`

### Problem

A versão inicial precisa ser fechada com qualidade.

### Scope

- Revisar docs.
- Rodar validações.
- Criar tag `v0.1.0`.
- Atualizar changelog.
- Garantir CI verde.

### Out of scope

- Novas features.

### Acceptance criteria

- Release notes criadas.
- CI verde.
- README final revisado.
- Demo manual concluída.
