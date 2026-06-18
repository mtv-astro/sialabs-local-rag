from __future__ import annotations

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    app: str
    environment: str


class PublicConfigResponse(BaseModel):
    app_name: str
    llm_provider: str
    llm_model: str
    embedding_provider: str
    embedding_model: str
    retrieval_top_k: int
    chunk_size: int
    chunk_overlap: int


class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    content: str = Field(min_length=10, max_length=1_000_000)
    source_type: str = Field(default="manual", min_length=1, max_length=40)


class DocumentResponse(BaseModel):
    id: str
    title: str
    source_type: str
    total_chars: int
    total_chunks: int
    created_at: str
    updated_at: str


class DocumentListResponse(BaseModel):
    documents: list[DocumentResponse]


class SourceChunk(BaseModel):
    chunk_id: str
    document_id: str
    document_title: str
    chunk_index: int
    score: float
    content: str


class ChatRequest(BaseModel):
    question: str = Field(min_length=3, max_length=4000)
    top_k: int | None = Field(default=None, ge=1, le=12)


class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceChunk]
    provider: str
    model: str
    retrieval_top_k: int
    latency_ms: int
