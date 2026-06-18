# ADR 0001 — Local-first RAG

## Status

Proposto

## Contexto

O projeto precisa demonstrar IA aplicada e soberania digital em um escopo pequeno e funcional. Documentos do usuário podem conter informação sensível, e o objetivo de portfólio é evidenciar controle sobre dados e modelos.

## Decisão

A aplicação será local-first no MVP. Documentos, embeddings, banco e geração de resposta devem rodar na máquina do usuário após download dos modelos.

## Consequências positivas

- Fortalece narrativa de privacidade.
- Demonstra uso de modelos locais.
- Reduz dependência de APIs comerciais.
- Facilita explicação de soberania digital com aplicação real.

## Consequências negativas

- Setup exige Ollama/modelos.
- Performance depende do hardware.
- Avaliador pode preferir demo gravada se não quiser baixar modelos.

## Alternativas consideradas

- API externa de LLM: mais simples, mas enfraquece a proposta local-first.
- Fine-tuning: desnecessário para consulta documental.
- SaaS multiusuário: escopo grande demais para MVP de portfólio.
