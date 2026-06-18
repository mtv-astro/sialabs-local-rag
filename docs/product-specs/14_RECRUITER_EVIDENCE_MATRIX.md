# Recruiter Evidence Matrix

## 1. Objetivo

Este documento conecta competências profissionais a evidências concretas que devem aparecer no repositório.

A ideia é evitar que o projeto pareça apenas uma demo visual. Cada parte do repo deve demonstrar uma capacidade avaliável.

## 2. Matriz principal

| Competência | Evidência no projeto | Onde o recrutador vê | Talking point |
|---|---|---|---|
| Produto | PRD, escopo, personas, critérios de aceite | `docs/01_PRD.md` | “Comecei definindo problema, usuário, MVP e limites.” |
| Full stack | Frontend + backend integrados | `frontend/`, `backend/` | “Implementei fluxo completo da UI até persistência e IA local.” |
| Frontend | Dashboard, upload, chat, painel de fontes | `frontend/src/` | “A UI mostra estados reais: loading, erro, vazio e sucesso.” |
| Backend | API REST com serviços separados | `backend/src/` | “Separei rotas, serviços, adapters e persistência.” |
| Banco de dados | Modelagem de documents/chunks/messages/traces | migrations, `docs/06_DATA_MODEL.md` | “Modelei dados para rastreabilidade do RAG.” |
| IA aplicada | RAG com embeddings, retrieval e geração | `docs/05_RAG_AI_SPEC.md` | “Não é só prompt: tem ingestão, chunking, vector search e fontes.” |
| IA local | Gemma 4 + EmbeddingGemma via Ollama | `.env.example`, adapters | “O fluxo principal roda localmente após baixar os modelos.” |
| Segurança em LLM | Prompt injection guardrails | testes, `docs/09_SECURITY_PRIVACY.md` | “Trato documentos como dados não confiáveis.” |
| Testes | Unit/integration tests | `backend/tests/`, CI | “Ollama é mockável; testes não dependem de modelo real.” |
| CI/CD | GitHub Actions | `.github/workflows/` | “Todo PR valida lint, testes, typecheck e build.” |
| Docker/Infra | Docker Compose local | `docker-compose.yml` | “Documentei execução reprodutível.” |
| Documentação | README, docs, ADRs | `README.md`, `docs/` | “O repo explica decisões, trade-offs e limites.” |
| Operação GitHub | Issues, PRs, commits limpos | GitHub history | “Usei fluxo incremental com rastreabilidade.” |
| Comunicação | Demo guide e case study | `docs/15_DEMO_AND_CASE_STUDY_GUIDE.md` | “Preparei o projeto para ser avaliado rapidamente.” |

## 3. Competências técnicas específicas

### TypeScript/React

Evidências:

- componentes reutilizáveis;
- chamadas API tipadas;
- estados de loading/erro;
- build passando;
- interface responsiva.

### Python/FastAPI

Evidências:

- Pydantic schemas;
- serviços testáveis;
- error handling;
- OpenAPI;
- pytest/mypy/ruff.

### SQL/dados

Evidências:

- migrations;
- índices;
- relações entre documentos, chunks e traces;
- deduplicação por hash;
- modelagem descrita.

### IA/RAG

Evidências:

- chunking configurável;
- embeddings locais;
- retrieval com scores;
- prompt seguro;
- resposta com fontes;
- trace do pipeline.

### Infraestrutura

Evidências:

- Docker Compose;
- healthchecks;
- `.env.example`;
- logs;
- documentação de setup.

## 4. Evidências operacionais

O repositório deve mostrar:

- issues com problema, escopo e critérios;
- branches pequenas;
- commits padronizados;
- PRs com summary/validation;
- CI verde;
- main limpa;
- release `v0.1.0`.

## 5. Perguntas prováveis em entrevista

### Por que local-first?

Resposta esperada:

> Porque o problema central envolve privacidade e autonomia. O projeto demonstra que é possível criar uma aplicação útil de IA sem enviar documentos para APIs externas no fluxo principal.

### Por que RAG?

Resposta esperada:

> RAG permite conectar o LLM a uma base específica sem treinar modelo. Isso reduz alucinação, permite fontes e torna o sistema mais auditável.

### Por que não fine-tuning?

Resposta esperada:

> Fine-tuning é desnecessário para o MVP. O problema é consulta sobre documentos locais. RAG é mais simples, barato, reversível e apropriado.

### Como você lidou com hallucination?

Resposta esperada:

> O sistema recupera fontes, aplica threshold e instrui o modelo a responder apenas com base no contexto. Quando não há evidência suficiente, retorna uma resposta de insuficiência.

### Como você testou sem depender do modelo real?

Resposta esperada:

> Criei interfaces/adapters para chat e embeddings. Nos testes, uso clientes fake para validar regras do domínio e API sem baixar modelo no CI.

### Qual trade-off do SQLite?

Resposta esperada:

> SQLite reduz fricção local e combina com MVP single-user. Para multiusuário ou produção maior, a evolução natural seria PostgreSQL com pgvector.

## 6. O que destacar no README

Adicionar seção:

```md
## Competências demonstradas

- Full stack com React + FastAPI
- IA local com Gemma 4 via Ollama
- RAG com embeddings, retrieval e fontes
- Segurança básica contra prompt injection
- SQLite, migrations e modelagem de dados
- Docker Compose e setup local
- Testes, typecheck, lint e CI
- Processo GitHub com issues e PRs
```

## 7. O que mostrar em screenshots

1. Dashboard com modelos disponíveis.
2. Upload de documento.
3. Biblioteca com status `ready`.
4. Chat respondendo com fontes.
5. Painel de fontes.
6. GitHub Actions verde.
7. PR com summary/validation.

## 8. Critério de impacto

O projeto será forte se um avaliador conseguir dizer:

> “Este candidato não apenas chama uma API de IA; ele entende produto, RAG, dados, segurança, testes, deploy local e processo de entrega.”
