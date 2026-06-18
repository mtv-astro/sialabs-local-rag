# Risk Register

## 1. Visão geral

Este registro lista riscos técnicos, operacionais e de apresentação do projeto.

| ID | Risco | Probabilidade | Impacto | Mitigação | Status |
|---|---|---:|---:|---|---|
| R-01 | Hardware local insuficiente para modelo grande | Média | Alto | Modelo configurável; default menor | Aberto |
| R-02 | Ollama não instalado no ambiente do avaliador | Alta | Médio | README claro; status acionável; demo gravada | Aberto |
| R-03 | PDF escaneado sem texto | Média | Médio | Documentar OCR fora do MVP; erro claro | Aberto |
| R-04 | Resposta alucinada | Média | Alto | Fontes, threshold, prompt restritivo | Aberto |
| R-05 | Prompt injection em documento | Média | Alto | Contexto delimitado; teste específico | Aberto |
| R-06 | Setup muito complexo | Média | Alto | Docker Compose, `.env.example`, troubleshooting | Aberto |
| R-07 | PRs grandes e difíceis de revisar | Média | Médio | Backlog em issues pequenas | Aberto |
| R-08 | CI falhar por depender de modelo real | Alta | Alto | Mocks para Ollama no CI | Aberto |
| R-09 | Banco local commitado acidentalmente | Baixa | Alto | `.gitignore`; checklist; CI simples | Aberto |
| R-10 | Projeto parecer acadêmico demais | Média | Médio | README focado em problema, demo e stack | Aberto |
| R-11 | UI consumir tempo demais | Média | Médio | Usar shadcn/ui e escopo visual simples | Aberto |
| R-12 | Vector store atrasar entrega | Média | Médio | Fallback de cosine similarity em Python | Aberto |

## 2. Riscos críticos

### R-01 — Hardware insuficiente

Descrição: Gemma 4 em variantes maiores pode exigir recursos que nem toda máquina possui.

Mitigação:

- Configurar modelo via `.env`.
- Documentar perfis: leve, padrão, workstation.
- Não bloquear projeto em modelo grande.

### R-04 — Resposta alucinada

Descrição: O LLM pode responder além dos documentos.

Mitigação:

- Retrieval com threshold.
- Prompt de insuficiência.
- Fontes obrigatórias.
- Testes de pergunta fora da base.

### R-05 — Prompt injection

Descrição: Documentos importados podem tentar alterar comportamento do assistente.

Mitigação:

- Tratar documentos como dados não confiáveis.
- Não dar ferramentas ao modelo no MVP.
- Testar documento malicioso.

### R-08 — CI depender de modelo local

Descrição: GitHub Actions não deve baixar e rodar LLM pesado.

Mitigação:

- Interfaces e mocks.
- Testes unitários sem Ollama real.
- Testes manuais locais documentados para modelo real.

## 3. Riscos de escopo

Itens que devem ser evitados no MVP:

- autenticação completa;
- multiusuário;
- agentes autônomos;
- OCR;
- multimodalidade avançada;
- deploy público;
- fine-tuning;
- integração com WhatsApp/Notion/Drive.

## 4. Gatilhos de corte

Cortar funcionalidades quando:

- uma feature exigir mais de um PR grande;
- CI ficar instável;
- a feature não melhorar a demo principal;
- o setup ficar difícil de explicar.

## 5. Estratégia de comunicação

Sempre comunicar limites como decisões conscientes, não como falhas.

Exemplo:

> “OCR ficou fora do MVP porque o foco da versão inicial é validar o pipeline local de RAG textual com fontes. A arquitetura permite adicionar OCR depois.”
