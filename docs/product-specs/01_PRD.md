# PRD — SIALabs Local RAG — Local Knowledge Assistant

## 1. Contexto

O projeto **SIALabs Local RAG** nasce como um experimento de IA aplicada e soberania digital, mas deve ser produzido com padrão de engenharia profissional. A aplicação permite que uma pessoa crie uma base de conhecimento local a partir de documentos e converse com esses documentos usando um LLM local.

O produto deve ser desenvolvido como vitrine técnica. Cada decisão precisa ajudar o avaliador a enxergar capacidade de produto, código, arquitetura, testes, documentação e operação.

## 2. Objetivo do produto

Criar uma aplicação web local-first que permita importar documentos e fazer perguntas sobre eles usando um pipeline de RAG com modelos locais.

A versão inicial deve ser funcional, testável, documentada e demonstrável.

## 3. Objetivo de portfólio

Demonstrar, em um único projeto pequeno, as seguintes competências:

| Competência | Evidência esperada |
|---|---|
| Produto | PRD, escopo, user stories, critérios de aceite |
| Frontend | Interface responsiva com upload, biblioteca e chat |
| Backend | API REST, validação, tratamento de erro, serviços internos |
| Dados | Modelagem de documentos, chunks, mensagens e traces |
| IA aplicada | RAG, embeddings, prompt engineering, respostas com fontes |
| Local AI | Gemma 4 e EmbeddingGemma via runtime local |
| Segurança | privacidade local, prompt injection, limites de upload |
| Operação | Docker, `.env.example`, healthchecks, logs |
| Qualidade | lint, testes, typecheck, CI |
| GitHub | issues, branches, commits, PRs e main limpa |

## 4. Personas

### 4.1 Usuário local

Pessoa que tem documentos em texto/PDF e quer fazer perguntas sem enviar os dados para APIs externas.

Necessidades:

- importar documentos com facilidade;
- receber respostas úteis;
- ver de onde veio a resposta;
- manter dados locais;
- rodar em máquina própria.

### 4.2 Recrutador técnico

Pessoa que avalia a qualidade do projeto e a capacidade do desenvolvedor.

Necessidades:

- entender o projeto em poucos minutos;
- ver README claro;
- identificar stack e arquitetura;
- conferir testes, CI e PRs;
- observar decisões realistas;
- avaliar autonomia técnica.

### 4.3 Tech lead / avaliador

Pessoa que analisa profundidade técnica.

Necessidades:

- ver separação de responsabilidades;
- entender trade-offs;
- conferir tratamento de erro;
- entender como RAG foi implementado;
- ver segurança mínima;
- ver evolução incremental.

## 5. Problemas a resolver

1. Usuários não querem enviar documentos privados para APIs externas.
2. Muitos projetos de IA não demonstram engenharia além do prompt.
3. Muitos portfólios não mostram processo: issues, PRs, validação e documentação.
4. RAG pode gerar respostas sem fonte, dificultando confiança.
5. Aplicações de IA local podem ser difíceis de instalar se não houver boa documentação.

## 6. Hipótese

Se o projeto oferecer uma aplicação local-first de RAG com fontes, boa UX, instalação clara, CI e documentação técnica, então ele será uma peça de portfólio forte para oportunidades em desenvolvimento full stack, automação e IA aplicada.

## 7. Métricas de sucesso

### Métricas de produto

- Usuário consegue importar pelo menos 3 documentos locais.
- Usuário consegue perguntar sobre os documentos importados.
- Resposta apresenta pelo menos uma fonte quando há contexto suficiente.
- Sistema informa claramente quando não há base suficiente para responder.
- Fluxo principal pode ser demonstrado em menos de 5 minutos.

### Métricas técnicas

- Backend possui testes unitários para chunking, parsing, retrieval e regras de resposta.
- API possui testes de integração para endpoints principais.
- Frontend passa em lint/typecheck/build.
- CI executa validações em PR.
- `.env.example` cobre todas as variáveis necessárias.
- Não há dependência obrigatória de API externa para o fluxo principal após download dos modelos.

### Métricas de recrutamento

- README explica o projeto, stack, arquitetura, comandos e demo.
- O repositório tem issues e PRs com títulos padronizados.
- A documentação explica trade-offs e limites do MVP.
- Há matriz explícita conectando competências a evidências no repositório.

## 8. Requisitos funcionais

### RF-01 — Verificar ambiente local de IA

O sistema deve verificar se o Ollama está acessível e se os modelos configurados estão disponíveis.

Critérios:

- Mostrar status do backend.
- Mostrar status do Ollama.
- Mostrar modelo de chat configurado.
- Mostrar modelo de embedding configurado.
- Exibir erro acionável se o modelo não estiver disponível.

### RF-02 — Importar documento

O usuário deve conseguir importar documentos `.txt`, `.md` e `.pdf`.

Critérios:

- Aceitar upload via interface.
- Validar extensão e tamanho.
- Calcular hash do arquivo para deduplicação.
- Persistir metadados.
- Marcar status de processamento.

### RF-03 — Extrair texto

O sistema deve extrair texto dos documentos suportados.

Critérios:

- `.txt` e `.md` lidos como texto.
- `.pdf` processado com biblioteca apropriada.
- Erros de parsing devem ser registrados.
- Documento inválido não pode quebrar o sistema.

### RF-04 — Criar chunks

O sistema deve dividir o texto em chunks rastreáveis.

Critérios:

- Cada chunk deve ter `document_id`, índice, texto, contagem aproximada de tokens/caracteres e metadados.
- O chunking deve ter sobreposição configurável.
- Chunks vazios devem ser descartados.

### RF-05 — Gerar embeddings locais

O sistema deve gerar embeddings para cada chunk usando modelo local.

Critérios:

- Usar adaptador de embeddings.
- Implementação inicial via Ollama `/api/embed`.
- Modelo recomendado: `embeddinggemma`.
- Falhas devem deixar documento em status `failed` com mensagem clara.

### RF-06 — Buscar contexto relevante

O sistema deve recuperar chunks relevantes para uma pergunta.

Critérios:

- Converter pergunta em embedding.
- Buscar top-k chunks mais similares.
- Aplicar threshold mínimo configurável.
- Retornar score, documento e chunk.

### RF-07 — Gerar resposta fundamentada

O sistema deve chamar Gemma 4 local para gerar resposta com base nos chunks recuperados.

Critérios:

- Prompt deve separar instruções do sistema, pergunta do usuário e contexto recuperado.
- Conteúdo recuperado deve ser tratado como dado não confiável.
- Resposta deve citar fontes por índice de chunk.
- Se não houver contexto suficiente, responder que não é possível concluir com base nos documentos.

### RF-08 — Exibir chat

O usuário deve conseguir conversar com a base.

Critérios:

- Campo de pergunta.
- Histórico de mensagens.
- Indicador de carregamento.
- Painel de fontes.
- Mensagem de erro clara quando o Ollama não responder.

### RF-09 — Gerenciar biblioteca

O usuário deve ver documentos importados e seus status.

Critérios:

- Lista de documentos.
- Status: `uploaded`, `processing`, `ready`, `failed`.
- Quantidade de chunks.
- Data de importação.
- Ação de remover documento.

### RF-10 — Expor traces de RAG

O sistema deve registrar e exibir dados básicos do pipeline.

Critérios:

- Pergunta.
- Chunks recuperados.
- Scores.
- Modelo usado.
- Tempo aproximado de embedding, retrieval e geração.

## 9. Requisitos não funcionais

### RNF-01 — Local-first

O fluxo principal deve funcionar localmente, sem envio de documentos a serviços externos.

### RNF-02 — Portabilidade

O projeto deve rodar em ambiente local via comandos documentados e preferencialmente via Docker Compose.

### RNF-03 — Segurança mínima

- Upload com limite de tamanho.
- Sanitização de nome de arquivo.
- Não executar conteúdo de documento.
- Não expor servidor para rede pública por padrão.
- Não commitar `.env` real.

### RNF-04 — Observabilidade

- Logs estruturados no backend.
- Healthcheck.
- Erros previsíveis com mensagens acionáveis.

### RNF-05 — Testabilidade

- Serviços de parsing, chunking, retrieval e prompt devem ser testáveis isoladamente.
- Ollama deve ser mockável em testes.

### RNF-06 — Manutenibilidade

- Separar rotas, serviços, adapters, modelos de dados e configuração.
- Evitar lógica pesada diretamente em endpoints.
- Documentar decisões arquiteturais em ADRs.

## 10. Escopo por versão

### v0.1 — MVP de portfólio

- Backend FastAPI.
- Frontend React.
- Upload `.txt`, `.md`, `.pdf`.
- Chunking.
- Embeddings com Ollama.
- Chat com Gemma 4.
- Citações simples.
- SQLite local.
- Docker Compose.
- CI básico.
- README e docs.

### v0.2 — Polimento técnico

- Melhor painel de traces.
- Busca híbrida lexical + semântica.
- Export/import da base.
- Modo benchmark.
- Testes e2e.
- Melhor UX de erros.

### v0.3 — Extensões demonstráveis

- Suporte a múltiplas bases.
- Re-ranking local.
- Avaliação automática de respostas.
- Deploy local em VPS protegida.
- Modo multimodal experimental se hardware permitir.

## 11. Critérios de aceite do MVP

A versão `v0.1` está pronta quando:

- O README permite rodar o projeto localmente.
- O usuário importa documentos suportados.
- O sistema processa chunks e embeddings.
- O chat responde com fontes.
- O sistema recusa resposta quando não há evidência suficiente.
- CI passa em PR.
- Não há segredos no repositório.
- Há documentação de arquitetura, segurança, testes e operação.
- Há roteiro de demo para recrutamento.

## 12. Principais riscos

| Risco | Impacto | Mitigação |
|---|---:|---|
| Hardware fraco para Gemma 4 maior | Alto | Permitir modelo configurável e default menor |
| PDF com extração ruim | Médio | Documentar limite e tratar erro |
| Resposta alucinar | Alto | Prompt com fontes, threshold e resposta de incerteza |
| Setup complexo | Alto | Docker, `.env.example`, healthcheck e troubleshooting |
| PRs grandes demais | Médio | Backlog em issues pequenas |
| Exposição do Ollama na rede | Alto | Bind local por padrão e documentação de segurança |
