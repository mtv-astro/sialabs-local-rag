# Executive Brief — SIALabs Local RAG — Local Knowledge Assistant

## Resumo

O **SIALabs Local RAG** é uma aplicação web local-first para consulta inteligente de documentos privados. O usuário importa arquivos, o sistema cria uma base semântica local e o chat responde perguntas usando um modelo Gemma 4 executado localmente via Ollama.

O projeto foi desenhado como peça de portfólio técnico. Ele precisa ser simples o suficiente para ser entregue em pequenos PRs, mas robusto o suficiente para demonstrar maturidade em engenharia de software, IA aplicada, documentação, segurança, testes e operação.

## Problema

Muitas aplicações de IA dependem de APIs externas e enviam dados do usuário para terceiros. Para documentos pessoais, materiais de trabalho, bases internas e conhecimento sensível, isso cria barreiras de privacidade e autonomia.

Ao mesmo tempo, projetos de portfólio de IA muitas vezes ficam restritos a prompts soltos, demos superficiais ou integrações com APIs comerciais. Este projeto resolve os dois pontos: demonstra IA útil, com arquitetura local, dados sob controle do usuário e rastreabilidade técnica.

## Proposta de valor

Uma aplicação local que transforma documentos em uma base consultável por IA, mantendo:

- execução local;
- privacidade por padrão;
- respostas baseadas em fontes;
- transparência do pipeline de RAG;
- arquitetura simples e testável;
- documentação profissional.

## Público-alvo do produto

O produto é pensado para um usuário técnico ou semi-técnico que deseja consultar documentos locais sem depender de API externa.

Para o portfólio, o público real é:

- recrutadores técnicos;
- tech leads;
- avaliadores de vaga júnior/pleno inicial;
- clientes potenciais de automação/IA;
- pessoas interessadas em IA local e soberania digital.

## Por que este projeto é bom para recrutamento

Ele evidencia uma combinação rara em projetos pequenos:

- visão de produto;
- implementação full stack;
- domínio de backend e APIs;
- noções de banco e modelagem;
- IA aplicada com RAG;
- preocupação com privacidade;
- entendimento de segurança em LLMs;
- Docker e execução local;
- CI/CD e qualidade;
- documentação clara.

## Escopo do MVP

O MVP deve permitir:

1. Rodar backend, frontend e dependências localmente.
2. Verificar status do Ollama e dos modelos configurados.
3. Importar documentos `.txt`, `.md` e `.pdf`.
4. Processar documentos em chunks.
5. Gerar embeddings locais.
6. Consultar a base via busca semântica.
7. Fazer perguntas em chat.
8. Receber respostas com citações aos trechos usados.
9. Ver painel de fontes e rastros básicos de recuperação.
10. Rodar lint, testes, typecheck e build em CI.

## Fora do escopo do MVP

- SaaS multiusuário.
- Login social.
- Cobrança/pagamentos.
- Treinamento ou fine-tuning de modelos.
- Agentes com ações externas autônomas.
- Deploy público sem autenticação.
- Sincronização com Google Drive, Notion ou WhatsApp.
- Suporte completo a áudio, vídeo e imagens.

## Resultado técnico esperado

Ao final da versão `v0.1`, o repositório deve conter:

- README forte;
- documentação em `docs/`;
- backend testado;
- frontend funcional;
- banco local versionado por migrations;
- Docker Compose local;
- GitHub Actions;
- issues e PRs limpos;
- demonstração gravável em poucos minutos.

## Sinal de maturidade

O diferencial do projeto não será a complexidade bruta. Será a clareza com que ele demonstra uma sequência profissional: problema, escopo, arquitetura, implementação incremental, validação local, CI, documentação e apresentação.
