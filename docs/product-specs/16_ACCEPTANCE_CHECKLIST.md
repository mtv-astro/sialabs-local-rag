# Acceptance Checklist

## 1. Produto

- [ ] PRD existe e está atualizado.
- [ ] Escopo do MVP está claro.
- [ ] Fora de escopo está claro.
- [ ] README explica valor do projeto.
- [ ] Demo principal funciona.

## 2. Backend

- [ ] FastAPI inicia localmente.
- [ ] `/health` retorna 200.
- [ ] `/api/models/status` verifica Ollama/modelos.
- [ ] Upload aceita `.txt`, `.md`, `.pdf`.
- [ ] Upload recusa tipos inválidos.
- [ ] Parser extrai texto.
- [ ] Chunking funciona.
- [ ] Embeddings são gerados.
- [ ] Retrieval retorna chunks.
- [ ] Chat retorna resposta com fontes.
- [ ] Sem contexto suficiente retorna mensagem de insuficiência.
- [ ] Traces são persistidos.

## 3. Frontend

- [ ] Dashboard mostra status.
- [ ] Biblioteca lista documentos.
- [ ] Upload via UI funciona.
- [ ] Chat envia pergunta.
- [ ] Resposta aparece no histórico.
- [ ] Fontes aparecem em painel.
- [ ] Erros são acionáveis.
- [ ] UI é responsiva o suficiente para demo.

## 4. Banco e dados

- [ ] Migrations funcionam.
- [ ] Documentos têm hash.
- [ ] Chunks têm índice e metadados.
- [ ] Embeddings são associados a chunks.
- [ ] Remover documento remove chunks/embeddings.
- [ ] `data/` está no `.gitignore`.

## 5. IA/RAG

- [ ] Modelo de chat é configurável.
- [ ] Modelo de embedding é configurável.
- [ ] Prompt separa contexto e pergunta.
- [ ] Documentos são tratados como dados não confiáveis.
- [ ] Teste de prompt injection passa.
- [ ] Resposta usa fontes.
- [ ] Trace mostra chunks e scores.

## 6. Segurança e privacidade

- [ ] `.env` real não está versionado.
- [ ] `.env.example` existe.
- [ ] Upload tem limite de tamanho.
- [ ] Nome de arquivo é sanitizado.
- [ ] CORS não usa `*` em configuração recomendada.
- [ ] README explica que dados ficam locais no fluxo principal.
- [ ] README explica limites de segurança.

## 7. Testes e qualidade

- [ ] `ruff check` passa.
- [ ] `pytest` passa.
- [ ] `mypy` passa.
- [ ] frontend lint passa.
- [ ] frontend typecheck passa.
- [ ] frontend build passa.
- [ ] CI verde no GitHub.

## 8. Operação

- [ ] Docker Compose documentado.
- [ ] Healthchecks existem.
- [ ] Comandos PowerShell documentados.
- [ ] Troubleshooting documentado.

## 9. GitHub

- [ ] Issues criadas.
- [ ] Branches seguem padrão.
- [ ] Commits seguem Conventional Commits.
- [ ] PRs têm summary e validation.
- [ ] PRs referenciam issues.
- [ ] Main está limpa.
- [ ] Release `v0.1.0` criada.

## 10. Recrutamento

- [ ] README tem seção de competências demonstradas.
- [ ] Há screenshots ou GIF.
- [ ] Há guia de demo.
- [ ] Há matriz de evidências.
- [ ] Há explicação de trade-offs.
- [ ] Há roadmap futuro.
