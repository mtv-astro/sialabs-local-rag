from __future__ import annotations

from time import perf_counter

from sialabs_local_rag.chunking import chunk_text
from sialabs_local_rag.prompting import SYSTEM_PROMPT, build_rag_prompt
from sialabs_local_rag.providers import ChatProvider, EmbeddingProvider
from sialabs_local_rag.schemas import ChatResponse, DocumentResponse
from sialabs_local_rag.settings import Settings
from sialabs_local_rag.storage import ChunkInput, Storage


class EmptyDocumentError(ValueError):
    """Raised when text cannot produce valid chunks."""


class RagService:
    """Application service for ingestion and retrieval augmented generation."""

    def __init__(
        self,
        settings: Settings,
        storage: Storage,
        embedding_provider: EmbeddingProvider,
        chat_provider: ChatProvider,
    ) -> None:
        self.settings = settings
        self.storage = storage
        self.embedding_provider = embedding_provider
        self.chat_provider = chat_provider

    async def ingest_text(self, title: str, content: str, source_type: str) -> DocumentResponse:
        chunks = chunk_text(
            content,
            chunk_size=self.settings.chunk_size,
            overlap=self.settings.chunk_overlap,
        )
        if not chunks:
            raise EmptyDocumentError("Document content did not produce any chunks.")

        embeddings = await self.embedding_provider.embed(chunks)
        chunk_inputs = [
            ChunkInput(index=index, content=chunk, embedding=embeddings[index])
            for index, chunk in enumerate(chunks)
        ]
        return self.storage.create_document(
            title=title.strip(),
            source_type=source_type.strip(),
            original_content=content,
            chunks=chunk_inputs,
        )

    async def answer_question(self, question: str, top_k: int | None = None) -> ChatResponse:
        started_at = perf_counter()
        selected_top_k = top_k or self.settings.retrieval_top_k
        query_embedding = (await self.embedding_provider.embed([question]))[0]
        sources = self.storage.search_chunks(query_embedding=query_embedding, top_k=selected_top_k)

        if not sources:
            answer = "Não encontrei documentos indexados para responder essa pergunta."
        else:
            user_prompt = build_rag_prompt(question=question, sources=sources)
            answer = await self.chat_provider.generate(
                system_prompt=SYSTEM_PROMPT,
                user_prompt=user_prompt,
            )

        latency_ms = int((perf_counter() - started_at) * 1000)
        self.storage.create_chat_record(
            question=question,
            answer=answer,
            provider=self.chat_provider.name,
            model=self.chat_provider.model,
            latency_ms=latency_ms,
            sources=sources,
        )

        return ChatResponse(
            answer=answer,
            sources=sources,
            provider=self.chat_provider.name,
            model=self.chat_provider.model,
            retrieval_top_k=selected_top_k,
            latency_ms=latency_ms,
        )
