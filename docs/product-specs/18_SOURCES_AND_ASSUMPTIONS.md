# Sources and Assumptions

## 1. Objetivo

Registrar fontes técnicas consultadas e premissas usadas para orientar a especificação.

## 2. Fontes oficiais e técnicas

### Gemma 4

- Google AI for Developers — Gemma 4 model overview  
  https://ai.google.dev/gemma/docs/core

- Google AI for Developers — Gemma 4 model card  
  https://ai.google.dev/gemma/docs/core/model_card_4

- Google AI for Developers — Run Gemma with Ollama  
  https://ai.google.dev/gemma/docs/integrations/ollama

- Ollama Library — Gemma 4  
  https://ollama.com/library/gemma4

### Embeddings

- Google AI for Developers — EmbeddingGemma model overview  
  https://ai.google.dev/gemma/docs/embeddinggemma

- Google Developers Blog — Introducing EmbeddingGemma  
  https://developers.googleblog.com/introducing-embeddinggemma/

- Ollama Docs — Embeddings  
  https://docs.ollama.com/capabilities/embeddings

- Ollama Library — EmbeddingGemma  
  https://ollama.com/library/embeddinggemma

### Segurança de aplicações com LLM

- OWASP Top 10 for Large Language Model Applications  
  https://owasp.org/www-project-top-10-for-large-language-model-applications/

- OWASP Gen AI Security — LLM01 Prompt Injection  
  https://genai.owasp.org/llmrisk/llm01-prompt-injection/

- NIST — AI Risk Management Framework: Generative AI Profile  
  https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## 3. Premissas do projeto

- O projeto será desenvolvido como portfólio público.
- O fluxo principal será local-first.
- O usuário pode instalar Ollama e baixar modelos.
- A aplicação será single-user no MVP.
- Documentos de demo serão fictícios.
- O CI não dependerá de rodar modelos pesados.
- O objetivo é demonstrar capacidade técnica e operacional, não criar um SaaS completo.

## 4. Premissas de stack

- React/Vite/TypeScript são adequados para frontend rápido e moderno.
- FastAPI é adequado para backend Python tipado e OpenAPI automático.
- SQLite é suficiente para MVP local.
- Ollama reduz fricção para rodar modelos locais.
- Gemma 4 é o motor de geração principal.
- EmbeddingGemma é a opção alinhada à narrativa de modelos locais e família Gemma.

## 5. Pontos que devem ser validados durante implementação

- Tag exata do modelo Gemma 4 mais adequada ao hardware local.
- Performance de `embeddinggemma` via Ollama no ambiente real.
- Melhor forma de persistir vetores no SQLite escolhido.
- Qualidade de extração de PDFs reais.
- Threshold inicial de similaridade.
- Tempos médios de geração.

## 6. Decisões reversíveis

- Trocar SQLite por PostgreSQL + pgvector.
- Trocar vector store local.
- Trocar modelo de embedding.
- Trocar variante de Gemma 4.
- Adicionar OCR.
- Adicionar reranking.
