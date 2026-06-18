from __future__ import annotations

from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_document_and_chat(client: TestClient) -> None:
    document_response = client.post(
        "/api/documents",
        json={
            "title": "SIALabs Portfolio",
            "content": (
                "SIALabs Local RAG é um projeto de portfólio que demonstra FastAPI, "
                "React, SQLite, RAG, embeddings locais e integração opcional com Ollama."
            ),
            "source_type": "manual",
        },
    )

    assert document_response.status_code == 201
    document = document_response.json()
    assert document["total_chunks"] >= 1

    chat_response = client.post(
        "/api/chat",
        json={"question": "Quais tecnologias o projeto demonstra?"},
    )

    assert chat_response.status_code == 200
    body = chat_response.json()
    assert body["provider"] == "mock"
    assert body["sources"]
    assert body["sources"][0]["document_title"] == "SIALabs Portfolio"


def test_duplicate_document_returns_conflict(client: TestClient) -> None:
    payload = {
        "title": "Documento duplicado",
        "content": "Conteúdo suficientemente grande para passar pela validação do MVP.",
        "source_type": "manual",
    }

    first = client.post("/api/documents", json=payload)
    second = client.post("/api/documents", json=payload)

    assert first.status_code == 201
    assert second.status_code == 409


def test_document_upload_rejects_unsupported_extension(client: TestClient) -> None:
    response = client.post(
        "/api/documents/upload",
        files={"file": ("dados.pdf", b"conteudo", "application/pdf")},
    )

    assert response.status_code == 415
