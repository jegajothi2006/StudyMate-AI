"""
app.py

StudyMate AI - a beginner-level AI-powered student utility application.

This app lets a student:
    1. Summarize Notes
    2. Explain a Concept
    3. Generate a Quiz
    4. Improve an Answer

It sends user input to an LLM (OpenAI API) using a specific, structured
prompt for each feature, and displays the AI's response in the interface.

Built for: ShadowFox AI Engineer Internship - Beginner Level Task 1
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, APIError, APIConnectionError, RateLimitError, AuthenticationError

from prompts import (
    build_summary_prompt,
    build_explain_prompt,
    build_quiz_prompt,
    build_improve_answer_prompt,
)

# ---------------------------------------------------------------------------
# SETUP
# ---------------------------------------------------------------------------

load_dotenv()  # loads variables from a local .env file

API_KEY = os.getenv("LLM_API_KEY")
MODEL_NAME = os.getenv("LLM_MODEL", "gpt-4o-mini")

st.set_page_config(page_title="StudyMate AI", page_icon="📚", layout="centered")


# ---------------------------------------------------------------------------
# CORE FUNCTION: CALL THE LLM
# ---------------------------------------------------------------------------

def call_llm(prompt: str) -> str:
    """
    Sends a prompt to the LLM API and returns the text response.

    Raises a plain Python exception with a user-friendly message if
    something goes wrong (missing key, network issue, rate limit, etc).
    The calling code is responsible for catching this and showing it
    to the user instead of a raw traceback.
    """
    if not API_KEY:
        raise RuntimeError(
            "No API key found. Please set LLM_API_KEY in your .env file."
        )

    client = OpenAI(api_key=API_KEY)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for students."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        content = response.choices[0].message.content
        if not content or not content.strip():
            raise RuntimeError("The AI returned an empty response. Please try again.")
        return content.strip()

    except AuthenticationError:
        raise RuntimeError(
            "Authentication failed. Your API key appears to be invalid. "
            "Please check the LLM_API_KEY value in your .env file."
        )
    except RateLimitError:
        raise RuntimeError(
            "The API rate limit or quota has been reached. Please wait a "
            "moment and try again, or check your API usage/billing."
        )
    except APIConnectionError:
        raise RuntimeError(
            "Could not connect to the AI service. Please check your "
            "internet connection and try again."
        )
    except APIError:
        raise RuntimeError(
            "The AI service returned an error while processing your "
            "request. Please try again in a moment."
        )
    except Exception:
        raise RuntimeError(
            "Something unexpected went wrong while contacting the AI "
            "service. Please try again."
        )


# ---------------------------------------------------------------------------
# VALIDATION HELPER
# ---------------------------------------------------------------------------

def validate_input(text: str, min_length: int = 5) -> str | None:
    """
    Checks the user's input before sending it to the API.

    Returns an error message string if invalid, or None if the input is
    valid.
    """
    if text is None or text.strip() == "":
        return "Please enter some content before submitting."
    if len(text.strip()) < min_length:
        return f"Your input looks too short. Please enter at least {min_length} characters."
    return None


# ---------------------------------------------------------------------------
# UI: HEADER
# ---------------------------------------------------------------------------

st.title("📚 StudyMate AI")
st.write(
    "An AI-powered study assistant that helps you **summarize notes**, "
    "**understand concepts**, **practice with quizzes**, and **improve your "
    "answers** — all in one simple tool."
)

if not API_KEY:
    st.warning(
        "No API key detected. Set `LLM_API_KEY` in a `.env` file before "
        "using the app. You can still explore the interface."
    )

# ---------------------------------------------------------------------------
# UI: SIDEBAR - CHOOSE UTILITY
# ---------------------------------------------------------------------------

st.sidebar.header("Choose a Utility")
utility = st.sidebar.radio(
    "What do you want to do?",
    (
        "Summarize Notes",
        "Explain a Concept",
        "Generate Quiz",
        "Improve My Answer",
    ),
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "StudyMate AI sends your input to an LLM using a task-specific prompt "
    "and returns the result below."
)

# ---------------------------------------------------------------------------
# UI: MAIN AREA - INPUT + OUTPUT PER UTILITY
# ---------------------------------------------------------------------------

st.subheader(utility)

if utility == "Summarize Notes":
    st.write("Paste your notes below and get a clean, structured summary.")
    user_input = st.text_area("Your notes:", height=220, placeholder="Paste your notes here...")
    button_label = "Summarize"
    prompt_builder = build_summary_prompt
    min_len = 20

elif utility == "Explain a Concept":
    st.write("Enter a concept or question and get a simple, student-friendly explanation.")
    user_input = st.text_area("Concept or question:", height=150, placeholder="e.g. What is recursion in programming?")
    button_label = "Explain"
    prompt_builder = build_explain_prompt
    min_len = 5

elif utility == "Generate Quiz":
    st.write("Enter a topic or study material and get a 5-question multiple-choice quiz.")
    user_input = st.text_area("Topic or study material:", height=200, placeholder="e.g. Photosynthesis, or paste a paragraph of notes...")
    button_label = "Generate Quiz"
    prompt_builder = build_quiz_prompt
    min_len = 10

else:  # Improve My Answer
    st.write("Paste your written answer and get an improved version with feedback.")
    user_input = st.text_area("Your answer:", height=200, placeholder="Paste your answer here...")
    button_label = "Improve Answer"
    prompt_builder = build_improve_answer_prompt
    min_len = 10

submit = st.button(button_label, type="primary")

# ---------------------------------------------------------------------------
# HANDLE SUBMISSION
# ---------------------------------------------------------------------------

if submit:
    error_message = validate_input(user_input, min_length=min_len)

    if error_message:
        st.error(error_message)
    else:
        prompt = prompt_builder(user_input)

        with st.spinner("Thinking... generating your result..."):
            try:
                result = call_llm(prompt)
            except RuntimeError as e:
                st.error(str(e))
                result = None

        if result:
            st.markdown("### Result")
            st.markdown(result)
