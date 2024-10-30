from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Dict, Optional

from .services import openai_service
from .dependencies import get_openai_service

router = APIRouter(prefix="/api", tags=["OpenAI API"])

@router.post("/generate_text")
async def generate_text(
    prompt: str,
    model: str = "text-davinci-003",
    max_tokens: Optional[int] = None,
    temperature: float = 0.7,
    top_p: Optional[float] = None,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
    stop: Optional[str] = None,
    openai_service: openai_service.OpenAIService = Depends(get_openai_service),
):
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
        JSONResponse: A JSON response containing the generated text.

    Raises:
        HTTPException: If an error occurs during API interaction.
    """
    try:
        response = await openai_service.generate_text(
            prompt,
            model,
            max_tokens,
            temperature,
            top_p,
            frequency_penalty,
            presence_penalty,
            stop,
        )
        return JSONResponse(response)
    except openai.error.APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {e}")

@router.post("/translate_text")
async def translate_text(
    text: str,
    target_language: str,
    model: str = "gpt-3.5-turbo",
    openai_service: openai_service.OpenAIService = Depends(get_openai_service),
):
    """
    Translates text using the OpenAI API.

    Args:
        text (str): The text to translate.
        target_language (str): The target language code (e.g., "fr" for French).
        model (str, optional): The OpenAI model to use. Defaults to "gpt-3.5-turbo".

    Returns:
        JSONResponse: A JSON response containing the translated text.

    Raises:
        HTTPException: If an error occurs during API interaction.
    """
    try:
        response = await openai_service.translate_text(
            text, target_language, model
        )
        return JSONResponse(response)
    except openai.error.APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating text: {e}")

@router.post("/complete_code")
async def complete_code(
    prompt: str,
    model: str = "code-davinci-002",
    max_tokens: Optional[int] = None,
    temperature: float = 0.7,
    top_p: Optional[float] = None,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
    stop: Optional[str] = None,
    openai_service: openai_service.OpenAIService = Depends(get_openai_service),
):
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
        JSONResponse: A JSON response containing the completed code.

    Raises:
        HTTPException: If an error occurs during API interaction.
    """
    try:
        response = await openai_service.complete_code(
            prompt,
            model,
            max_tokens,
            temperature,
            top_p,
            frequency_penalty,
            presence_penalty,
            stop,
        )
        return JSONResponse(response)
    except openai.error.APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error completing code: {e}")