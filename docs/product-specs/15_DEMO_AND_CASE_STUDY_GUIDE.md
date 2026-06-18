# Demo and Case Study Guide

## 1. Objetivo

Preparar o projeto para apresentação em README, LinkedIn, entrevista e conversa técnica.

A demo deve ser curta, objetiva e focada em evidências.

## 2. Roteiro de demo de 5 minutos

### 0:00 — Contexto

> “Este é o SIALabs Local RAG, um assistente local para consultar documentos usando modelos locais. A ideia é demonstrar IA aplicada com privacidade, RAG, frontend, backend, banco, Docker, testes e CI.”

### 0:30 — Status local

Mostrar dashboard:

- Backend ok.
- Ollama ok.
- Modelo de chat.
- Modelo de embedding.

Falar:

> “Antes de usar o chat, verifico se o runtime local e os modelos estão disponíveis.”

### 1:00 — Upload

Importar documento fictício.

Falar:

> “O backend valida o arquivo, extrai texto, quebra em chunks, gera embeddings e salva tudo localmente.”

### 2:00 — Pergunta respondida

Perguntar algo claramente presente no documento.

Falar:

> “A resposta não vem só do modelo. O sistema recupera trechos relevantes e usa esses trechos como contexto.”

### 3:00 — Fontes

Abrir painel de fontes.

Falar:

> “Cada resposta mostra os chunks usados, com documento, índice e score. Isso melhora auditabilidade.”

### 3:45 — Pergunta fora da base

Fazer pergunta que não está nos documentos.

Falar:

> “Quando não há evidência suficiente, o sistema deve dizer que não sabe com base na base local.”

### 4:20 — GitHub

Mostrar README, docs e CI.

Falar:

> “Também organizei o projeto como entrega profissional: issues, PRs, CI, testes e documentação.”

## 3. Case study para README

### Problema

Aplicações de IA geralmente enviam dados para APIs externas. Para documentos privados, isso reduz controle e cria barreiras de adoção.

### Solução

Construí uma aplicação local-first que usa RAG com modelos locais para responder perguntas sobre documentos importados.

### Stack

- React + Vite + TypeScript
- FastAPI + Python
- SQLite
- Ollama
- Gemma 4
- EmbeddingGemma
- Docker Compose
- GitHub Actions

### Resultado

- Upload de documentos.
- Chunking e embeddings locais.
- Busca semântica.
- Chat com fontes.
- Traces de RAG.
- CI e documentação.

### Decisões técnicas

- Usei RAG em vez de fine-tuning porque a necessidade era consultar documentos locais.
- Usei SQLite no MVP para reduzir fricção de setup.
- Usei adapters para Ollama para permitir testes com mocks.
- Tratei documentos como dados não confiáveis para mitigar prompt injection.

### Limitações

- PDF escaneado não tem OCR no MVP.
- Performance depende do hardware local.
- Busca vetorial inicial é simples e pode evoluir para pgvector ou reranking.

### Próximos passos

- Busca híbrida.
- Reranking local.
- E2E tests.
- OCR local.
- Multi-base.

## 4. Post curto para LinkedIn

```text
Construí o SIALabs Local RAG, um projeto de portfólio focado em IA local e RAG.

A aplicação permite importar documentos, gerar embeddings localmente e conversar com a base usando Gemma 4 via Ollama, com respostas acompanhadas de fontes.

O objetivo foi demonstrar mais do que uma demo de prompt: arquitetura full stack, backend FastAPI, frontend React, SQLite, pipeline RAG, Docker, testes, CI e documentação técnica.

Principais aprendizados:
- como estruturar um pipeline RAG auditável;
- como isolar integrações com modelos locais;
- como tratar documentos como dados não confiáveis;
- como transformar o histórico do GitHub em evidência de processo profissional.
```

## 5. Perguntas de demo sugeridas

Usar documentos fictícios criados para o projeto.

1. “Qual é o objetivo deste projeto?”
2. “Quais tecnologias são usadas?”
3. “Como o sistema protege a privacidade dos documentos?”
4. “Quais são as limitações do MVP?”
5. “O que este documento diz sobre prompt injection?”
6. “Qual é a política de férias da empresa?” — se não estiver nos docs, deve retornar insuficiência.

## 6. Checklist antes de gravar vídeo

- [ ] Repositório limpo.
- [ ] README atualizado.
- [ ] CI verde.
- [ ] App rodando.
- [ ] Documentos demo sem dados reais.
- [ ] Modelo baixado.
- [ ] Perguntas testadas.
- [ ] Respostas com fontes.
- [ ] Pergunta fora da base retorna insuficiência.
- [ ] Screenshots atualizados.

## 7. Estrutura de README final

```md
# SIALabs Local RAG

## Overview
## Demo
## Features
## Architecture
## Local AI Models
## Tech Stack
## Getting Started
## Usage
## Security and Privacy
## Testing
## GitHub Workflow
## Roadmap
## Portfolio Evidence
## License
```
