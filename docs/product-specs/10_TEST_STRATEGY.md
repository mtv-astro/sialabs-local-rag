# Test Strategy

## 1. Objetivo

Garantir que o projeto tenha evidências objetivas de qualidade sem tornar o MVP pesado demais.

A estratégia de testes deve focar no núcleo técnico: parsing, chunking, embeddings mockados, retrieval, prompt, API e estados principais do frontend.

## 2. Pirâmide de testes

```text
Muitos testes unitários
Alguns testes de integração de API
Poucos testes e2e para fluxo principal
```

## 3. Backend

### Unit tests

Ferramenta: `pytest`

Cobrir:

- normalização de texto;
- chunking com overlap;
- deduplicação por hash;
- validação de extensão;
- montagem de prompt;
- decisão de insuficiência de contexto;
- parsing de resposta;
- tratamento de erro de Ollama.

### Integration tests

Ferramentas: `pytest`, `httpx`, `TestClient`.

Cobrir:

- `GET /health`;
- `GET /api/models/status` com Ollama mockado;
- `POST /api/documents` com `.txt`;
- recusa de arquivo inválido;
- `POST /api/search` com vector store fake;
- `POST /api/chat` com LLM mockado;
- `GET /api/rag/traces/{id}`.

### Contract tests

Validar schemas Pydantic para requests/responses.

## 4. Frontend

### Unit/component tests

Ferramenta: Vitest + Testing Library.

Cobrir:

- `StatusBadge`;
- `DocumentList`;
- `ChatMessageBubble`;
- `SourcePanel`;
- estados de erro.

### Build validation

Comandos:

```powershell
npm run lint
npm run typecheck
npm run build
```

### E2E opcional

Ferramenta: Playwright.

Fluxo mínimo:

1. abrir app;
2. ver status;
3. importar documento fake;
4. fazer pergunta;
5. ver resposta e fontes.

No CI, pode usar backend com mocks para não depender de Ollama real.

## 5. Testes de IA/RAG

### Dataset de teste

Criar `backend/tests/fixtures/docs/` com documentos pequenos e fictícios.

Exemplos:

- `privacy_policy.md`
- `project_notes.md`
- `prompt_injection.md`

### Casos obrigatórios

| Caso | Esperado |
|---|---|
| Pergunta presente no documento | Retorna chunk relevante |
| Pergunta fora da base | Retorna insuficiência |
| Documento com prompt injection | Não obedece instrução do documento |
| Documento duplicado | Retorna 409 ou não duplica |
| PDF sem texto | Erro tratado |

## 6. Mocks

Ollama não deve ser dependência obrigatória em testes de CI.

Criar fakes:

- `FakeEmbeddingClient`
- `FakeChatClient`
- `InMemoryVectorStore`

Isso permite testar domínio e API sem baixar modelos.

## 7. Comandos de validação local

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

Repo completo:

```powershell
git status --short
git diff --stat
```

## 8. Cobertura mínima sugerida

Não transformar cobertura em fetiche. Para portfólio, o mais importante é cobrir partes críticas.

Meta recomendada:

- domínio/RAG core: 80%+
- API principal: rotas críticas cobertas
- frontend: componentes críticos e build passando

## 9. Testes manuais de aceite

Antes de release `v0.1`:

- [ ] Rodar app do zero usando README.
- [ ] Ver status do modelo.
- [ ] Importar `.md`.
- [ ] Importar `.txt`.
- [ ] Importar `.pdf` simples.
- [ ] Fazer pergunta respondida.
- [ ] Ver fontes.
- [ ] Fazer pergunta fora da base.
- [ ] Remover documento.
- [ ] Rodar CI localmente quando possível.

## 10. Evidência para recrutamento

No README, incluir badges e bloco de validação:

```text
Validation
- ruff check
- pytest
- mypy
- frontend build
- GitHub Actions passing
```

No PR, sempre listar comandos executados.
