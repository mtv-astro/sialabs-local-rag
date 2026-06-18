# Security and Privacy

## Princípio

O MVP é local-first. Dados de documentos ficam no ambiente do usuário e não são enviados para APIs externas por padrão.

## Dados persistidos

- Metadados de documentos.
- Chunks textuais.
- Embeddings em JSON.
- Perguntas e respostas de chat para rastreabilidade técnica.

## O que não deve ser commitado

- `.env` real.
- Tokens.
- Chaves de API.
- Dados reais de clientes.
- Dumps de banco com conteúdo sensível.
- Modelos baixados.

## Limitações de segurança do MVP

- Não há autenticação.
- Não há autorização por usuário.
- Não há criptografia de banco local.
- Não há política de retenção por usuário.

Portanto, não exponha a aplicação publicamente sem uma issue específica de hardening.

## Recomendações futuras

- Proteger endpoints administrativos.
- Adicionar autenticação local ou reverse proxy autenticado.
- Implementar limpeza/expiração de histórico de chat.
- Separar datasets por workspace.
- Adicionar varredura de segredos no CI.
