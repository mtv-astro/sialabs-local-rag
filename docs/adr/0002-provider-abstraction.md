# ADR 0002 — Provider abstraction

## Status

Accepted

## Context

CI e ambientes de avaliação não devem depender de modelo local, GPU ou download pesado.

## Decision

Separar providers em contratos de embedding e chat:

- `hash` e `mock` para CI/demo.
- `ollama` para execução com IA local real.

## Consequences

- Testes ficam rápidos e determinísticos.
- Integração real continua disponível.
- O código demonstra design substituível e testável.
