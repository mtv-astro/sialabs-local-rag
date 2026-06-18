from __future__ import annotations

import re

_WHITESPACE_RE = re.compile(r"\s+")


def normalize_text(text: str) -> str:
    """Normalize text while preserving semantic content."""

    return _WHITESPACE_RE.sub(" ", text).strip()


def estimate_tokens(text: str) -> int:
    """Cheap token estimate for operational metadata."""

    return max(1, len(text) // 4)


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 180) -> list[str]:
    """Split text into overlapping chunks suitable for local RAG."""

    normalized = normalize_text(text)
    if not normalized:
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    if overlap < 0:
        raise ValueError("overlap must be zero or positive")
    if overlap >= chunk_size:
        overlap = max(0, chunk_size // 4)

    chunks: list[str] = []
    start = 0
    text_length = len(normalized)

    while start < text_length:
        end = min(start + chunk_size, text_length)

        if end < text_length:
            min_boundary = start + int(chunk_size * 0.6)
            boundary = normalized.rfind(" ", min_boundary, end)
            if boundary > start:
                end = boundary

        segment = normalized[start:end].strip()
        if segment:
            chunks.append(segment)

        if end >= text_length:
            break

        start = max(0, end - overlap)
        while start < text_length and normalized[start].isspace():
            start += 1

    return chunks
