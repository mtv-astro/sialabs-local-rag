# .env.example

```env
APP_ENV=local
APP_NAME=sialabs-local-rag
APP_VERSION=0.1.0

BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000
BACKEND_CORS_ORIGINS=http://localhost:5173

DATABASE_URL=sqlite:///./data/sialabs_local_rag.db

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_CHAT_MODEL=gemma4:e4b
OLLAMA_EMBED_MODEL=embeddinggemma

RAG_TOP_K=5
RAG_MIN_SCORE=0.25
RAG_CHUNK_SIZE=1200
RAG_CHUNK_OVERLAP=180
RAG_MAX_CONTEXT_CHARS=9000
RAG_TEMPERATURE=0.2

UPLOAD_MAX_MB=20
UPLOAD_ALLOWED_EXTENSIONS=.txt,.md,.pdf

# Required only if exposing admin endpoints outside localhost.
ADMIN_API_KEY=<local-admin-api-key>
```
