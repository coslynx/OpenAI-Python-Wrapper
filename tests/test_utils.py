import pytest
from unittest.mock import patch

from app.utils import openai_utils
from app.services import openai_service

# Import the OpenAI API client from the openai library
import openai

# Load environment variables from .env
from app.config import Config

# Initialize the OpenAI API client
openai.api_key = Config.OPENAI_API_KEY

class MockOpenAIObject:
    def __init__(self, choices, **kwargs):
        self.choices = choices
        self.__dict__.update(kwargs)

@pytest.fixture
def mock_openai_utils():
    with patch("app.utils.openai_utils.OpenAIUtils") as mock_utils:
        mock_utils.return_value.generate_text.return_value = MockOpenAIObject(
            choices=[{"text": "This is some generated text."}]
        )
        mock_utils.return_value.translate_text.return_value = MockOpenAIObject(
            choices=[{"message": {"content": "Ceci est une traduction."}}]
        )
        mock_utils.return_value.complete_code.return_value = MockOpenAIObject(
            choices=[{"text": "print('Hello, world!')"}]
        )
        yield mock_utils

def test_generate_text(mock_openai_utils):
    openai_utils_instance = openai_utils.OpenAIUtils()
    response = openai_utils_instance.generate_text(prompt="Write a short sentence.")
    assert response.choices[0].text == "This is some generated text."

def test_translate_text(mock_openai_utils):
    openai_utils_instance = openai_utils.OpenAIUtils()
    response = openai_utils_instance.translate_text(text="This is a translation.", target_language="fr")
    assert response.choices[0].message.content == "Ceci est une traduction."

def test_complete_code(mock_openai_utils):
    openai_utils_instance = openai_utils.OpenAIUtils()
    response = openai_utils_instance.complete_code(prompt="print('Hello, ")
    assert response.choices[0].text == "print('Hello, world!')"

def test_openai_service_generate_text(mock_openai_utils):
    service = openai_service.OpenAIService()
    response = service.generate_text(prompt="Write a short sentence.")
    assert response["text"] == "This is some generated text."

def test_openai_service_translate_text(mock_openai_utils):
    service = openai_service.OpenAIService()
    response = service.translate_text(text="This is a translation.", target_language="fr")
    assert response["translation"] == "Ceci est une traduction."

def test_openai_service_complete_code(mock_openai_utils):
    service = openai_service.OpenAIService()
    response = service.complete_code(prompt="print('Hello, ")
    assert response["code"] == "print('Hello, world!')"