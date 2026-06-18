# Product Spec

## 1. Visão do produto

O produto é um assistente local de conhecimento. Ele não tenta competir com ferramentas SaaS completas de gestão documental. O foco é demonstrar uma experiência útil, local e confiável: importar documentos, fazer perguntas e ver as fontes.

## 2. Princípios de produto

1. **Local por padrão**: documentos e prompts não devem sair da máquina no fluxo principal.
2. **Fonte antes de fluência**: uma resposta bonita sem fonte é pior que uma resposta simples com evidência.
3. **Erro acionável**: quando algo falhar, a interface deve orientar o próximo passo.
4. **Escopo pequeno**: cada funcionalidade deve caber em uma issue clara.
5. **Demonstração rápida**: o fluxo principal deve ser compreensível em poucos minutos.

## 3. Jornada principal

1. Usuário abre a aplicação.
2. Sistema mostra status do backend, Ollama e modelos.
3. Usuário importa documentos.
4. Sistema processa arquivos e exibe status.
5. Usuário faz uma pergunta.
6. Sistema busca chunks relevantes.
7. Sistema chama Gemma 4 com contexto recuperado.
8. Usuário recebe resposta com fontes.
9. Usuário abre o painel de fontes e confere os trechos usados.

## 4. User stories

### US-01 — Ver status do ambiente

Como usuário local, quero ver se backend, Ollama e modelos estão prontos para saber se posso usar o chat.

Critérios:

- Status visível na tela inicial.
- Erro mostra comando sugerido, como `ollama pull gemma4:e4b` ou modelo configurado.
- O sistema não tenta gerar resposta se o modelo estiver indisponível.

### US-02 — Importar documentos

Como usuário, quero importar arquivos `.txt`, `.md` e `.pdf` para criar minha base de conhecimento.

Critérios:

- Upload aceita arquivos suportados.
- Arquivos não suportados são recusados.
- Status de processamento é visível.
- Documento processado aparece como `ready`.

### US-03 — Fazer pergunta sobre documentos

Como usuário, quero perguntar sobre os documentos importados para obter respostas contextualizadas.

Critérios:

- Campo de pergunta disponível.
- Resposta aparece no histórico.
- Fontes aparecem anexadas à resposta.
- Sistema informa quando não há contexto suficiente.

### US-04 — Conferir fontes

Como usuário, quero ver os trechos usados na resposta para avaliar confiança.

Critérios:

- Cada fonte mostra nome do documento, índice do chunk e trecho.
- Fonte inclui score aproximado de similaridade.
- O painel permite copiar trecho.

### US-05 — Remover documento

Como usuário, quero remover documentos da base para controlar meus dados locais.

Critérios:

- Remover documento apaga metadados, chunks e embeddings relacionados.
- Ação pede confirmação.
- Biblioteca atualiza após remoção.

### US-06 — Entender limitações

Como recrutador/avaliador, quero entender limites do MVP para avaliar maturidade técnica.

Critérios:

- README explica limites.
- Docs explicam trade-offs.
- Sistema não promete precisão absoluta.

## 5. Estados da interface

### Tela inicial

- Status do ambiente.
- Ações rápidas: importar documento, abrir chat, ver documentação.
- Aviso de privacidade local.

### Biblioteca de documentos

- Lista com nome, tipo, tamanho, status, chunks, data.
- Ações: ver detalhes, remover.

### Chat

- Histórico de mensagens.
- Input de pergunta.
- Botão enviar.
- Painel lateral de fontes.
- Estado de carregamento.
- Erros legíveis.

### Configurações

- Modelo de chat atual.
- Modelo de embedding atual.
- Base URL do Ollama.
- Top-k e threshold.
- Somente leitura no MVP; edição via `.env` para evitar complexidade.

## 6. Mensagens de erro esperadas

| Situação | Mensagem sugerida |
|---|---|
| Ollama indisponível | `Ollama não está acessível em OLLAMA_BASE_URL. Verifique se o serviço está rodando.` |
| Modelo ausente | `Modelo não encontrado. Rode: ollama pull <modelo>` |
| Arquivo inválido | `Tipo de arquivo não suportado. Use .txt, .md ou .pdf.` |
| PDF sem texto | `Não foi possível extrair texto deste PDF. PDFs escaneados exigem OCR, fora do MVP.` |
| Sem documentos | `Importe ao menos um documento antes de perguntar.` |
| Sem contexto suficiente | `Não encontrei evidência suficiente nos documentos para responder com segurança.` |

## 7. Regras de UX importantes

- Nunca esconder que a resposta vem de IA.
- Mostrar fontes por padrão quando houver resposta.
- Diferenciar falha técnica de ausência de evidência.
- Evitar telas complexas demais no MVP.
- Manter design limpo, técnico e profissional.

## 8. Conteúdo de exemplo para demo

Usar documentos fictícios e seguros, por exemplo:

- `demo/company-handbook.md`
- `demo/project-notes.txt`
- `demo/architecture-overview.md`

Não usar documentos reais com dados pessoais ou informações sensíveis.
