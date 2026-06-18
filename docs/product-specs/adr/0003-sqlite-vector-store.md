# ADR 0003 — SQLite como banco local do MVP

## Status

Proposto

## Contexto

A aplicação é single-user e local-first. O setup deve ser simples para portfólio.

## Decisão

Usar SQLite no MVP para metadados, documentos, chunks, mensagens e traces. A busca vetorial pode usar extensão local ou fallback com cosine similarity em Python para reduzir risco de entrega.

## Consequências positivas

- Baixa fricção.
- Fácil reset.
- Sem serviço externo obrigatório.
- Coerente com local-first.

## Consequências negativas

- Menos adequado para multiusuário.
- Busca vetorial pode ser menos performática.
- Extensões vetoriais podem aumentar complexidade.

## Evolução futura

PostgreSQL + pgvector se o projeto evoluir para deploy, multiusuário ou bases maiores.
