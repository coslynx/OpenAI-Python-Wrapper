"""
This module provides utility functions for interacting with the OpenAI API.

It encapsulates common logic for sending requests, processing responses,
and handling errors, making it easier to integrate OpenAI capabilities
within other components of the MVP.

This module adheres to the following design principles:

- Modularity:  Encapsulates API-related logic, making the codebase more organized and reusable.
- Abstraction:  Provides a clean interface for other components to interact with the OpenAI API.
- Robustness:  Implements error handling for potential API failures and data inconsistencies.
- Scalability:  The code is designed for future expansion and handling increased request volumes.
"""

import os
from typing import Dict, Any, Optional

import openai
from fastapi import HTTPException

# Load environment variables from .env
from .config import Config

# Initialize the OpenAI API client
openai.api_key = Config.OPENAI_API_KEY

class OpenAIUtils:
    """
    Provides a utility class for interacting with the OpenAI API.

    This class handles API calls, data transformations, and error handling.
    """

    def __init__(self):
        """Initializes the OpenAIUtils class."""
        pass

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
    ) -> openai.OpenAIObject:
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
            stop (str, optional): A sequence of strings to stop generation at. Defaults to None.

        Returns:
            openai.OpenAIObject: The response from the OpenAI API.

        Raises:
            HTTPException: If an error occurs during API interaction.
        """
        try:
            response = await openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop,
            )
            return response
        except openai.error.APIError as e:
            raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating text: {e}")

    async def translate_text(
        self,
        text: str,
        target_language: str,
        model: str = "gpt-3.5-turbo",
    ) -> openai.OpenAIObject:
        """
        Translates text using the OpenAI API.

        Args:
            text (str): The text to translate.
            target_language (str): The target language code (e.g., "fr" for French).
            model (str, optional): The OpenAI model to use. Defaults to "gpt-3.5-turbo".

        Returns:
            openai.OpenAIObject: The response from the OpenAI API.

        Raises:
            HTTPException: If an error occurs during API interaction.
        """
        try:
            response = await openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "user", "content": f"Translate this text into {target_language}: {text}"},
                ],
            )
            return response
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
    ) -> openai.OpenAIObject:
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
            openai.OpenAIObject: The response from the OpenAI API.

        Raises:
            HTTPException: If an error occurs during API interaction.
        """
        try:
            response = await openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop,
            )
            return response
        except openai.error.APIError as e:
            raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error completing code: {e}")