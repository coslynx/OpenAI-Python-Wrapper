"""
This module implements the core business logic for interacting with the OpenAI API.

It provides functions for performing various AI tasks like text generation, translation,
code completion, and more. This service acts as an abstraction layer over the OpenAI API,
offering a clean interface for other components in the MVP.

The main logic is implemented in the `openai_service` class, which uses the `openai_utils`
module for handling API calls and data transformations.

This module adheres to the following design principles:

- **Modularity:** Encapsulates API-related logic, making the codebase more organized and reusable.
- **Abstraction:**  Provides a clean interface for other components to interact with the OpenAI API.
- **Robustness:** Implements error handling for potential API failures and data inconsistencies.
- **Scalability:**  The code is designed for future expansion and handling increased request volumes.
"""
import os
from typing import Dict, Any, Optional

import openai
from fastapi import HTTPException

from .utils import openai_utils

# Load environment variables from .env
from .config import Config

# Initialize the OpenAI API client
openai.api_key = Config.OPENAI_API_KEY


class OpenAIService:
    """
    Provides a service layer for interacting with the OpenAI API.

    This class offers functions for text generation, translation, code completion,
    and other AI-related tasks. It handles API calls and data transformations
    through the `openai_utils` module.
    """

    def __init__(self):
        """Initializes the OpenAIService."""
        self.openai_utils = openai_utils.OpenAIUtils()

    async def generate_text(
        self,
        prompt: str,
        model: str = "text-davinci-003",
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        top_p: Optional[float] = None,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
        stop: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Generates text using the OpenAI API.

        Args:
            prompt (str): The prompt to use for text generation.
            model (str, optional): The OpenAI model to use. Defaults to "text-davinci-003".
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to None.
            temperature (float, optional): The temperature to use for sampling. Defaults to 0.7.
            top_p (float, optional): The top_p value for sampling. Defaults to None.
            frequency_penalty (float, optional): The frequency penalty to use. Defaults to 0.0.
            presence_penalty (float, optional): The presence penalty to use. Defaults to 0.0.
            stop (str, optional):  A sequence of strings to stop generation at. Defaults to None.

        Returns:
            Dict[str, Any]: A dictionary containing the generated text.

        Raises:
            HTTPException: If an error occurs during API interaction.
        """

        try:
            response = await self.openai_utils.generate_text(
                prompt,
                model,
                max_tokens,
                temperature,
                top_p,
                frequency_penalty,
                presence_penalty,
                stop,
            )
            return {"text": response.choices[0].text}
        except openai.error.APIError as e:
            raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating text: {e}")

    async def translate_text(
        self,
        text: str,
        target_language: str,
        model: str = "gpt-3.5-turbo",
    ) -> Dict[str, Any]:
        """
        Translates text using the OpenAI API.

        Args:
            text (str): The text to translate.
            target_language (str): The target language code (e.g., "fr" for French).
            model (str, optional): The OpenAI model to use. Defaults to "gpt-3.5-turbo".

        Returns:
            Dict[str, Any]: A dictionary containing the translated text.

        Raises:
            HTTPException: If an error occurs during API interaction.
        """

        try:
            response = await self.openai_utils.translate_text(text, target_language, model)
            return {"translation": response.choices[0].message.content}
        except openai.error.APIError as e:
            raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error translating text: {e}")

    async def complete_code(
        self,
        prompt: str,
        model: str = "code-davinci-002",
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        top_p: Optional[float] = None,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
        stop: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Completes code using the OpenAI API.

        Args:
            prompt (str): The prompt to use for code completion.
            model (str, optional): The OpenAI model to use. Defaults to "code-davinci-002".
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to None.
            temperature (float, optional): The temperature to use for sampling. Defaults to 0.7.
            top_p (float, optional): The top_p value for sampling. Defaults to None.
            frequency_penalty (float, optional): The frequency penalty to use. Defaults to 0.0.
            presence_penalty (float, optional): The presence penalty to use. Defaults to 0.0.
            stop (str, optional): A sequence of strings to stop generation at. Defaults to None.

        Returns:
            Dict[str, Any]: A dictionary containing the completed code.

        Raises:
            HTTPException: If an error occurs during API interaction.
        """

        try:
            response = await self.openai_utils.complete_code(
                prompt,
                model,
                max_tokens,
                temperature,
                top_p,
                frequency_penalty,
                presence_penalty,
                stop,
            )
            return {"code": response.choices[0].text}
        except openai.error.APIError as e:
            raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error completing code: {e}")