# Security and Privacy Spec

## 1. Objetivo

Garantir que o projeto demonstre uso responsável de IA local, sem prometer segurança absoluta. A aplicação deve ser segura o suficiente para MVP local e bem documentada quanto aos riscos.

## 2. Princípios

1. **Dados locais por padrão**.
2. **Nenhum segredo no Git**.
3. **Documentos são dados não confiáveis**.
4. **LLM não executa ações sensíveis**.
5. **Erros não vazam conteúdo desnecessário**.
6. **Deploy público exige autenticação**.

## 3. Privacidade

### Garantias do MVP

- Documentos enviados ficam na máquina local.
- Embeddings são gerados localmente.
- Respostas são geradas localmente.
- Banco local fica em `./data/`.
- `.env` real não é versionado.

### Limites

- O usuário precisa baixar modelos previamente.
- Logs/traces podem conter trechos de documentos; por isso não devem ser enviados a serviços externos no MVP.
- Se o usuário alterar configurações para APIs externas no futuro, isso deve ser explicitamente indicado.

## 4. Riscos de LLM

### Prompt injection

Risco: documento importado contém instruções que tentam manipular o assistente.

Mitigações:

- Delimitar contexto.
- System prompt diz que documentos são dados não confiáveis.
- Não permitir ferramentas externas no MVP.
- Teste automatizado com prompt injection.

### Sensitive information disclosure

Risco: o assistente revelar conteúdo sensível importado pelo próprio usuário.

Mitigações:

- Aplicação single-user local.
- Avisar que documentos importados aparecem nas respostas.
- Não incluir dados reais em demos públicas.

### Misinformation/hallucination

Risco: modelo responder além dos documentos.

Mitigações:

- Responder apenas com base no contexto.
- Exigir fontes.
- Retornar insuficiência quando não houver contexto.
- Mostrar chunks usados.

### Vector/embedding weakness

Risco: retrieval ruim leva a resposta errada.

Mitigações:

- Threshold configurável.
- Trace dos chunks recuperados.
- Testes com dataset controlado.
- Futuro reranking.

### Unbounded consumption

Risco: documentos grandes ou perguntas repetidas sobrecarregarem máquina local.

Mitigações:

- Limite de upload.
- Limite de chunks por documento no MVP se necessário.
- Timeout de chamada ao Ollama.
- `RAG_MAX_CONTEXT_CHARS`.

## 5. Segurança de upload

Regras:

- Aceitar apenas `.txt`, `.md`, `.pdf`.
- Validar extensão e MIME quando possível.
- Sanitizar nome.
- Salvar fora de caminhos controlados pelo usuário.
- Impedir path traversal.
- Definir `UPLOAD_MAX_MB`.
- Não executar macros, scripts ou comandos.

## 6. Segurança de API

Para execução local:

- Bind padrão em `127.0.0.1`.
- CORS restrito ao frontend local.

Para deploy público:

- Não expor sem autenticação.
- Usar header `X-Admin-API-Key` ou autenticação adequada.
- Configurar HTTPS via proxy.
- Não expor Ollama diretamente.

## 7. Variáveis de ambiente

Toda variável deve aparecer em `.env.example`.

Nunca commitar:

- `.env`
- tokens reais
- chaves privadas
- bancos locais com dados reais
- uploads reais
- logs com conteúdo sensível

## 8. Headers e CORS

MVP local:

```env
BACKEND_CORS_ORIGINS=http://localhost:5173
```

Não usar `*` em ambiente exposto.

## 9. Logs

Logs devem incluir:

- request id;
- endpoint;
- status;
- duração;
- erro técnico.

Logs não devem incluir por padrão:

- documento completo;
- prompt completo;
- resposta completa;
- caminhos sensíveis do usuário.

## 10. Checklist de segurança

Antes de PR:

- [ ] `.env.example` atualizado.
- [ ] `.env` no `.gitignore`.
- [ ] `data/` no `.gitignore`.
- [ ] `uploads/` no `.gitignore`.
- [ ] upload limita extensão e tamanho.
- [ ] prompt injection testado.
- [ ] erro do Ollama tratado.
- [ ] CORS restrito.
- [ ] README explica limites.

## 11. Documentos de referência

Ver `docs/18_SOURCES_AND_ASSUMPTIONS.md` para fontes oficiais usadas na elaboração do plano.
