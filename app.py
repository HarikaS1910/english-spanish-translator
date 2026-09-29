"""Streamlit web interface for the English <-> Spanish LLM translator.

Run with:  streamlit run app.py
"""

import streamlit as st

from translator import DIRECTIONS, TranslationError, translate

st.set_page_config(page_title="EN ↔ ES Translator", page_icon="🌎")

st.title("🌎 English ↔ Spanish Translator")
st.caption("Powered by OpenAI GPT-4o")

# 1. Choose translation direction
direction = st.radio(
    "Translation direction",
    options=list(DIRECTIONS.keys()),
    horizontal=True,
)

# 2. Enter text
source_language = DIRECTIONS[direction][0]
text = st.text_area(
    f"Enter {source_language} text",
    height=150,
    placeholder="Type or paste your text here...",
)

# 3. Translate and show the result
if st.button("Translate", type="primary"):
    try:
        with st.spinner("Translating..."):
            result = translate(text, direction)
        st.subheader("Translation")
        st.success(result)
    except TranslationError as e:
        st.error(str(e))
