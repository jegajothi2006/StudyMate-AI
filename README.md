# StudyMate AI

An AI-powered student utility application built as the **ShadowFox AI Engineer Internship – Beginner Level Task 1**.

## Project Description

StudyMate AI is a simple, practical Streamlit web app that uses an LLM (Large Language Model) API to help students with everyday study tasks. Instead of being a generic chatbot, it offers four focused, purpose-built utilities, each with its own carefully structured prompt.

## Problem Statement

Students often spend a lot of time on repetitive study tasks: condensing long notes, understanding a confusing concept, creating practice questions, and polishing written answers before submission. StudyMate AI speeds up these specific tasks using AI, without requiring the student to write or manage prompts themselves.

## Features

1. **Summarize Notes** – Paste raw notes and receive a concise, structured summary.
2. **Explain a Concept** – Enter any concept or question and get a simple, student-friendly explanation with an example.
3. **Generate Quiz** – Enter a topic or study material and receive 5 multiple-choice questions (4 options each) with a separate answer key.
4. **Improve My Answer** – Paste a written answer and get an improved version (better grammar, clarity, and structure) plus feedback, without losing the original idea.

## Technologies Used

- **Python 3**
- **Streamlit** – for the web interface
- **OpenAI API** – the LLM used to generate responses (model configurable via `LLM_MODEL`, default `gpt-4o-mini`)
- **python-dotenv** – for loading the API key from a local `.env` file

No frameworks like LangChain, no vector databases, no agents, and no backend server are used. This is intentionally a simple, single-app project.

## How the Application Works

1. The user opens the Streamlit app and selects a utility from the sidebar (Summarize Notes, Explain a Concept, Generate Quiz, or Improve My Answer).
2. The user types or pastes their input into a text box.
3. When the user clicks the action button, the app first **validates** the input (checks it isn't empty or too short).
4. If valid, the app builds a **task-specific prompt** (from `prompts.py`) using the user's input.
5. The prompt is sent to the OpenAI API via `client.chat.completions.create(...)`.
6. While waiting, a loading spinner is shown.
7. The AI's response is displayed in the main panel in readable Markdown format.
8. If anything goes wrong (missing key, bad key, network issue, rate limit), a clear error message is shown instead of a crash or raw traceback.

## Project Structure

```
StudyMate-AI/
│
├── app.py            # Main Streamlit application (UI, validation, API calls)
├── prompts.py         # Structured prompt-builder functions, one per utility
├── requirements.txt   # Python dependencies
├── .env.example        # Template showing which environment variables are needed
├── .env                # Your real API key (create this yourself, never committed)
├── .gitignore          # Ensures .env and other local files are not committed
└── README.md
```

## Installation Steps

1. Clone or download this project folder.
2. Create a virtual environment and activate it (see commands below).
3. Install the dependencies from `requirements.txt`.
4. Create a `.env` file with your API key (see next section).
5. Run the app with Streamlit.

## Environment Variable / API Key Setup

The app reads your API key from an environment variable called `LLM_API_KEY`.

1. Copy `.env.example` to a new file named `.env`.
2. Open `.env` and replace the placeholder with your real OpenAI API key:

```
LLM_API_KEY=your_actual_api_key_here
```

3. (Optional) Set `LLM_MODEL` in `.env` if you want to use a different model than the default `gpt-4o-mini`.

The API key is **never** hard-coded in the source code — it is loaded at runtime using `python-dotenv`.

## How to Run the Application

### 1. Create a virtual environment
```bash
python -m venv venv
```

### 2. Activate it (Windows)
```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create and configure `.env`
```bash
copy .env.example .env
```
Then open `.env` in a text editor and paste in your real API key.

### 5. Run the Streamlit application
```bash
streamlit run app.py
```

The app will open automatically in your browser (usually at `http://localhost:8501`).

## Example Usage

**Explain a Concept**
- Input: `What is recursion in programming?`
- Output: A simple explanation of recursion with a small example (like calculating factorial), written in plain language.

**Generate Quiz**
- Input: `Photosynthesis`
- Output: 5 multiple-choice questions about photosynthesis, each with 4 options, followed by an answer key (e.g. "1. B").

## Error Handling

The app handles the following situations gracefully, without crashing:

- **Empty input** – Shows "Please enter some content before submitting." and does not call the API.
- **Very short input** – Shows a message asking for more content, based on a minimum character length per utility.
- **Missing/invalid API key** – Shows a clear authentication error message.
- **Network/connection failure** – Shows a message asking the user to check their internet connection.
- **Rate limit reached** – Shows a message asking the user to wait and try again.
- **Unexpected API errors** – Caught and shown as a generic friendly error rather than a Python traceback.

## Prompt Engineering Approach

Each utility has its own dedicated prompt-building function in `prompts.py` (not one generic prompt reused for everything). Every prompt explicitly defines:

- **Role** – what kind of assistant the AI should act as (e.g. "study assistant", "tutor", "writing coach").
- **Task** – exactly what to do with the input.
- **User input** – the student's actual content, clearly delimited.
- **Expected output/format** – for example, the quiz prompt requires exactly 5 questions, 4 options each, and a separate answer key in a fixed format; the "Improve My Answer" prompt requires an "Improved Answer" section followed by a "Feedback" section.

This keeps the AI's output consistent and predictable for each feature, rather than relying on one-size-fits-all instructions.

## Future Improvements

- Add the ability to upload a text file or PDF of notes instead of only pasting text.
- Allow the user to choose quiz difficulty or number of questions.
- Add a history/download option so students can save previous summaries or quizzes.
- Add support for switching between multiple LLM providers.

## Notes on Scope

This is intentionally a **beginner-level** project built for ShadowFox Task 1. It does not use RAG, LangChain, agents, vector databases, or any backend/database beyond the LLM API call itself, in line with the task requirements.
