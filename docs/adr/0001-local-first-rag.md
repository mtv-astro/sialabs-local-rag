# ADR 0001 — Local-first RAG

## Status

Accepted

## Context

O objetivo do projeto é evidenciar IA aplicada com soberania de dados e execução local.

## Decision

A aplicação será local-first: SQLite local, providers locais por padrão e integração opcional com Ollama.

## Consequences

- Recrutadores conseguem rodar o projeto sem cloud.
- O projeto comunica privacidade e autonomia.
- Escalabilidade fica limitada no MVP, mas a evolução para vector store externo é direta.
