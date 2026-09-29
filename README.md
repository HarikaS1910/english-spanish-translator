# English–Spanish Bidirectional LLM Translator

A web app that translates text between English and Spanish using OpenAI's GPT-4o.
Built with Python and Streamlit.

## Features
- Translate English → Spanish or Spanish → English
- Prompt templates that preserve tone and context, and handle idioms and grammar differences
- Streamlit interface for entering text, choosing direction, and viewing results
- Error handling for invalid keys, rate limits, empty input, and connection problems
- Evaluation script to compare model output against reference translations

## Tech Stack
Python, OpenAI API (GPT-4o), Streamlit, Prompt Engineering, REST APIs, JSON, Git, GitHub

## Setup

1. Clone the repo and open the folder
2. Create and activate a virtual environment

   Windows:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
   Mac/Linux:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install packages: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your OpenAI API key
5. Run the app: `streamlit run app.py`

## Project Structure
```
translator.py   # core translation logic and prompt templates
app.py          # Streamlit web interface
evaluate.py     # sample-sentence evaluation
```

## How It Works
1. The user enters text and picks a direction.
2. `translator.py` builds a system prompt with translation rules and sends it,
   with the text, to the GPT-4o REST API as JSON messages.
3. The JSON response is parsed and the translation is shown in the app.

## Evaluation
Run `python evaluate.py` to translate sample sentences (including idioms and
formal/informal phrasing) and compare them to human reference translations.
Results are saved to `evaluation_results.md`. Prompt wording was refined based on these comparisons.

## Notes
Built with the help of ChatGPT and AI-assisted coding tools to speed up development and debugging.
