import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import openai_service
from unittest.mock import patch


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@patch.object(openai_service.OpenAIService, "generate_text")
def test_generate_text(mock_generate_text, client):
    mock_generate_text.return_value = {"text": "This is some generated text."}
    response = client.post("/api/generate_text", json={"prompt": "Write a short sentence."})
    assert response.status_code == 200
    assert response.json() == {"text": "This is some generated text."}


@patch.object(openai_service.OpenAIService, "translate_text")
def test_translate_text(mock_translate_text, client):
    mock_translate_text.return_value = {"translation": "Ceci est une traduction."}
    response = client.post("/api/translate_text", json={"text": "This is a translation.", "target_language": "fr"})
    assert response.status_code == 200
    assert response.json() == {"translation": "Ceci est une traduction."}


@patch.object(openai_service.OpenAIService, "complete_code")
def test_complete_code(mock_complete_code, client):
    mock_complete_code.return_value = {"code": "print('Hello, world!')"}
    response = client.post("/api/complete_code", json={"prompt": "print('Hello, "})
    assert response.status_code == 200
    assert response.json() == {"code": "print('Hello, world!')"}