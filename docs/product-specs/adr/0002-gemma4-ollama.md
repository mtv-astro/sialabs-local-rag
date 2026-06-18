# ADR 0002 — Gemma 4 via Ollama

## Status

Proposto

## Contexto

O usuário quer demonstrar soberania em modelos locais. O projeto precisa de um runtime acessível e documentado para rodar modelos em ambiente local.

## Decisão

Usar Ollama como runtime local e Gemma 4 como modelo principal de geração. O modelo exato será configurável por `.env`, permitindo escolher variante conforme hardware.

## Consequências positivas

- Integração simples via HTTP.
- Boa experiência local.
- Permite usar variantes menores ou maiores.
- Facilita demo e documentação.

## Consequências negativas

- Depende de instalação local do Ollama.
- Tags e performance podem variar com o ambiente.
- CI não deve depender de modelo real.

## Mitigação

- Criar adapters e mocks.
- Validar status de modelos.
- Documentar comandos de pull.
- Manter modelo configurável.
