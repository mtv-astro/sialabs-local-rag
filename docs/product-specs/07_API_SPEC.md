# API Spec

## 1. Convenções

Base URL local:

```text
http://localhost:8000
```

Formato:

- JSON para payloads comuns.
- Multipart para upload.
- Erros no padrão `{ "detail": "...", "code": "..." }`.

## 2. Health

### GET `/health`

Retorna status do backend.

Resposta 200:

```json
{
  "status": "ok",
  "app": "sialabs-local-rag",
  "version": "0.1.0"
}
```

### GET `/api/models/status`

Verifica Ollama e modelos.

Resposta 200:

```json
{
  "ollama": {
    "status": "ok",
    "base_url": "http://localhost:11434"
  },
  "chat_model": {
    "name": "gemma4:e4b",
    "available": true
  },
  "embedding_model": {
    "name": "embeddinggemma",
    "available": true
  }
}
```

Resposta 503:

```json
{
  "detail": "Ollama não está acessível em http://localhost:11434",
  "code": "OLLAMA_UNAVAILABLE"
}
```

## 3. Documents

### POST `/api/documents`

Upload de documento.

Request:

- `multipart/form-data`
- campo `file`

Resposta 201:

```json
{
  "id": "doc_123",
  "filename": "notes.md",
  "status": "ready",
  "chunk_count": 8,
  "created_at": "2026-06-17T00:00:00Z"
}
```

Erros:

- 400 arquivo inválido.
- 409 duplicado.
- 503 embedding model indisponível.

### GET `/api/documents`

Lista documentos.

Resposta 200:

```json
{
  "items": [
    {
      "id": "doc_123",
      "filename": "notes.md",
      "status": "ready",
      "chunk_count": 8,
      "file_size": 14000,
      "created_at": "2026-06-17T00:00:00Z"
    }
  ]
}
```

### GET `/api/documents/{document_id}`

Detalhe do documento.

### DELETE `/api/documents/{document_id}`

Remove documento, chunks e embeddings.

Resposta 204.

### GET `/api/documents/{document_id}/chunks`

Lista chunks do documento.

Resposta 200:

```json
{
  "items": [
    {
      "id": "chunk_1",
      "chunk_index": 0,
      "text_preview": "Primeiros caracteres...",
      "char_start": 0,
      "char_end": 1200,
      "page_number": null
    }
  ]
}
```

## 4. Search

### POST `/api/search`

Busca semântica sem geração.

Request:

```json
{
  "query": "O que o documento diz sobre privacidade?",
  "top_k": 5
}
```

Resposta 200:

```json
{
  "items": [
    {
      "document_id": "doc_123",
      "document_title": "privacy.md",
      "chunk_id": "chunk_4",
      "chunk_index": 4,
      "score": 0.82,
      "text": "Trecho recuperado..."
    }
  ]
}
```

## 5. Chat

### POST `/api/chat/sessions`

Cria sessão.

Request:

```json
{
  "title": "Perguntas sobre docs"
}
```

Resposta 201:

```json
{
  "id": "session_123",
  "title": "Perguntas sobre docs",
  "created_at": "2026-06-17T00:00:00Z"
}
```

### POST `/api/chat`

Gera resposta.

Request:

```json
{
  "session_id": "session_123",
  "question": "Qual é a política de privacidade descrita?",
  "top_k": 5
}
```

Resposta 200:

```json
{
  "answer": "O documento afirma que os dados ficam locais... [doc:doc_123 chunk:4]",
  "sources": [
    {
      "document_id": "doc_123",
      "document_title": "privacy.md",
      "chunk_id": "chunk_4",
      "chunk_index": 4,
      "score": 0.82,
      "text": "Trecho recuperado..."
    }
  ],
  "trace_id": "trace_123"
}
```

### GET `/api/chat/sessions/{session_id}/messages`

Retorna histórico.

## 6. Traces

### GET `/api/rag/traces/{trace_id}`

Retorna detalhes do pipeline.

Resposta 200:

```json
{
  "id": "trace_123",
  "question": "Qual é a política de privacidade descrita?",
  "chat_model": "gemma4:e4b",
  "embedding_model": "embeddinggemma",
  "top_k": 5,
  "min_score": 0.25,
  "retrieval_ms": 120,
  "generation_ms": 6400,
  "retrieved_chunks": [
    {
      "document_id": "doc_123",
      "chunk_index": 4,
      "score": 0.82
    }
  ]
}
```

## 7. Segurança dos endpoints

No MVP local, a aplicação pode rodar sem autenticação quando bindada em `localhost`.

Se houver deploy em VPS ou rede pública, adicionar autenticação simples por header antes de expor endpoints administrativos:

```text
X-Admin-API-Key: <local-admin-api-key>
```

## 8. Contrato OpenAPI

Um rascunho de contrato está em:

```text
spec/openapi-draft.yaml
```
