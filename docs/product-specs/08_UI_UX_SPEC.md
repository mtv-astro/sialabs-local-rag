# UI/UX Spec

## 1. Objetivo da interface

A interface deve comunicar clareza, controle local e confiabilidade. O visual deve ser limpo, técnico e direto, evitando aparência de experimento inacabado.

## 2. Rotas frontend

| Rota | Função |
|---|---|
| `/` | Dashboard/status |
| `/documents` | Biblioteca de documentos |
| `/documents/:id` | Detalhe de documento e chunks |
| `/chat` | Chat com fontes |
| `/settings` | Configurações visíveis |
| `/about` | Explicação do projeto e privacidade |

## 3. Layout

### App shell

- Sidebar ou topbar simples.
- Logo/texto: `SIALabs Local RAG`.
- Indicador de status: Backend, Ollama, Modelos.
- Conteúdo principal centralizado.

### Dashboard

Cards:

- Backend: ok/erro.
- Ollama: ok/erro.
- Chat model: nome e status.
- Embedding model: nome e status.
- Documentos prontos.
- Última pergunta.

Ações:

- Importar documento.
- Abrir chat.
- Ver docs no GitHub.

### Biblioteca

Tabela/cards com:

- nome;
- tipo;
- tamanho;
- status;
- chunks;
- data;
- ações.

Estados:

- vazio: “Importe seu primeiro documento”.
- processamento: spinner discreto.
- erro: mensagem e detalhes.

### Chat

Layout sugerido:

```text
+---------------------------------------------+
| Histórico de mensagens                      |
|                                             |
| Usuário: ...                                |
| Assistente: ... [fontes]                    |
|                                             |
+----------------------+----------------------+
| Input pergunta       | Painel de fontes     |
+----------------------+----------------------+
```

Painel de fontes:

- documento;
- chunk;
- score;
- trecho;
- botão copiar.

## 4. Componentes

- `StatusBadge`
- `ModelStatusCard`
- `DocumentUploadDropzone`
- `DocumentList`
- `DocumentStatusPill`
- `ChatMessageBubble`
- `SourcePanel`
- `TraceSummary`
- `ErrorCallout`
- `EmptyState`

## 5. Tom de texto

Direto, técnico e acessível.

Exemplos:

- “Rodando localmente.”
- “Modelo não encontrado.”
- “Fonte usada na resposta.”
- “Não encontrei evidência suficiente nos documentos.”

## 6. Estados obrigatórios

### Loading

- Upload em andamento.
- Documento processando.
- Pergunta sendo respondida.

### Empty

- Sem documentos.
- Sem mensagens.
- Sem fontes.

### Error

- Ollama offline.
- Modelo ausente.
- Upload inválido.
- Falha na extração do PDF.
- Falha na geração da resposta.

### Success

- Documento pronto.
- Resposta com fontes.
- Healthcheck ok.

## 7. Acessibilidade mínima

- Labels em inputs.
- Contraste adequado.
- Botões com texto claro.
- Feedback visual e textual.
- Navegação por teclado nos botões principais.

## 8. Design system

Usar Tailwind e shadcn/ui para manter produtividade.

Componentes recomendados:

- Card
- Button
- Badge
- Alert
- Tabs
- Sheet/Drawer para fontes em telas pequenas
- Table
- Textarea
- Progress

## 9. Responsividade

- Desktop: chat + fontes lado a lado.
- Mobile/tablet: fontes em drawer ou abaixo da resposta.

## 10. Demonstração para recrutamento

A UI deve favorecer uma demo nesta ordem:

1. Mostrar status local.
2. Importar documento.
3. Mostrar chunks/status.
4. Fazer pergunta respondida.
5. Abrir fontes.
6. Fazer pergunta fora da base.
7. Mostrar resposta de insuficiência.
8. Abrir README/docs para explicar arquitetura.
