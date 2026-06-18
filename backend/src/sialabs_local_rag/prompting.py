from __future__ import annotations

from collections.abc import Sequence

from sialabs_local_rag.schemas import SourceChunk

SYSTEM_PROMPT = """
Você é o assistente local do SIALabs Local RAG.
Responda apenas com base nas fontes recuperadas.
Quando a resposta não estiver apoiada no contexto, diga que não encontrou evidência suficiente.
Priorize clareza, objetividade e transparência.
Não invente citações, dados ou conclusões que não estejam no contexto.
""".strip()


def build_rag_prompt(question: str, sources: Sequence[SourceChunk]) -> str:
    context_blocks = []
    for position, source in enumerate(sources, start=1):
        context_blocks.append(
            "\n".join(
                [
                    f"Fonte {position}",
                    f"Documento: {source.document_title}",
                    f"Chunk: {source.chunk_index}",
                    f"Score: {source.score}",
                    "Conteúdo:",
                    source.content,
                ]
            )
        )

    context = "\n\n---\n\n".join(context_blocks)
    return f"""
Pergunta do usuário:
{question}

Contexto recuperado:
{context}

Instruções de resposta:
- Responda em português.
- Use apenas o contexto recuperado.
- Seja direto.
- Quando útil, mencione os documentos usados.
- Não exponha detalhes internos do sistema.
""".strip()
