# Testing Strategy

## Objetivo

Garantir que o primeiro PR seja validável localmente e em CI sem exigir Ollama ou GPU.

## Camadas testadas

### Unitário

- Normalização e chunking.
- Similaridade vetorial.
- Normalização de vetores.

### API

- Healthcheck.
- Criação de documento.
- Chat com fontes usando mock/hash.
- Documento duplicado.
- Upload com extensão inválida.

### Frontend

- `npm run typecheck`.
- `npm run build`.

## Comandos

```powershell
cd backend
uv run ruff check . --fix
uv run ruff check .
uv run pytest
uv run mypy src
```

```powershell
cd frontend
npm ci
npm run typecheck
npm run build
```

## Estratégia de CI

O CI usa providers locais determinísticos, não Ollama. Isso evita falhas por hardware/modelos ausentes e mantém o pipeline rápido.

## Testes futuros

- Teste de integração com Ollama usando profile manual.
- Testes de upload Markdown real.
- Testes de parser PDF.
- Testes de latência em bases maiores.
- Testes de regressão de prompts.
