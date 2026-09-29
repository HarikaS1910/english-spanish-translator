"""Core translation logic for the English <-> Spanish LLM translator.

This file has no Streamlit code, so it can be reused by the web app
and by the evaluation script.
"""

import os

from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

load_dotenv()

MODEL = "gpt-4o"

# Direction -> (source language, target language)
DIRECTIONS = {
    "English → Spanish": ("English", "Spanish"),
    "Spanish → English": ("Spanish", "English"),
}

# Prompt template: tells the model HOW to translate, not just WHAT to translate.
SYSTEM_PROMPT_TEMPLATE = """You are a professional {source} to {target} translator.

Rules:
1. Preserve the meaning, context, and tone of the original (formal stays formal, casual stays casual).
2. Translate idioms and expressions by meaning, not word for word. Use a natural
   {target} equivalent when one exists.
3. Handle grammar differences correctly (gender agreement, verb conjugation,
   formal/informal "you" such as tú/usted, word order).
4. Keep names, numbers, URLs, and formatting (line breaks, punctuation) unchanged.
5. Keep polite words such as "please" and "thank you" (por favor, gracias).
   When translating into Spanish, use the polite "usted" form for requests
   unless the text is clearly casual.
6. Output ONLY the {target} translation. No explanations, notes, or quotation marks.
"""


class TranslationError(Exception):
    """Raised with a friendly message when translation fails."""


def build_system_prompt(direction: str) -> str:
    """Fill the prompt template for the chosen direction."""
    source, target = DIRECTIONS[direction]
    return SYSTEM_PROMPT_TEMPLATE.format(source=source, target=target)


def get_client() -> OpenAI:
    """Create the OpenAI client from the OPENAI_API_KEY environment variable."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise TranslationError(
            "OPENAI_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    return OpenAI(api_key=api_key)


def translate(text: str, direction: str = "English → Spanish") -> str:
    """Translate `text` in the given direction and return the translated string."""
    # Input processing
    text = (text or "").strip()
    if not text:
        raise TranslationError("Please enter some text to translate.")
    if direction not in DIRECTIONS:
        raise TranslationError(f"Unknown direction: {direction}")

    client = get_client()

    # JSON request: a list of role/content messages
    messages = [
        {"role": "system", "content": build_system_prompt(direction)},
        {"role": "user", "content": text},
    ]

    # Error handling around the REST API call
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.2,  # low = more consistent translations
        )
    except AuthenticationError:
        raise TranslationError("Your OpenAI API key looks invalid.")
    except RateLimitError:
        raise TranslationError("Rate limit or quota reached. Try again shortly.")
    except APIConnectionError:
        raise TranslationError("Could not reach OpenAI. Check your internet connection.")
    except APIStatusError as e:
        raise TranslationError(f"OpenAI API error ({e.status_code}). Please try again.")

    # JSON response: pull the text out of the first choice
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    # Quick manual test: python translator.py
    print(translate("Break a leg at your interview tomorrow!", "English → Spanish"))
    print(translate("Estoy muy emocionado por la oportunidad.", "Spanish → English"))
