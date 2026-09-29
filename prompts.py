"""
prompts.py

This file holds all the prompt-building functions for StudyMate AI.

Each function takes the user's raw input and returns a well-structured
prompt string that clearly tells the AI:
    - what role it should play
    - what task to perform
    - what the user provided
    - what output format is expected

Keeping prompts here (instead of writing them inline in app.py) makes the
main app file easier to read and makes it obvious how each feature is
"instructed" separately.
"""


def build_summary_prompt(notes: str) -> str:
    """Prompt for the 'Summarize Notes' feature."""
    prompt = f"""You are a helpful study assistant for a college student.

TASK:
Summarize the following notes into a clear, structured study summary.

REQUIREMENTS:
- Keep the summary concise but do not remove important concepts.
- Use bullet points for key ideas.
- Use short headings if the notes cover multiple topics.
- Do not add information that is not present in the notes.
- Write in simple, student-friendly language.

STUDENT NOTES:
\"\"\"
{notes}
\"\"\"

Now provide the structured summary.
"""
    return prompt


def build_explain_prompt(concept: str) -> str:
    """Prompt for the 'Explain a Concept' feature."""
    prompt = f"""You are a friendly tutor explaining topics to a college student
who wants a clear, simple explanation (not a research-level explanation).

TASK:
Explain the following concept or question in simple, easy-to-understand language.

REQUIREMENTS:
- Assume the student has only basic background knowledge.
- Avoid unnecessary jargon; if a technical term is required, briefly define it.
- Include one simple, relatable example if it helps understanding.
- Keep the explanation focused and not overly long.
- Structure the explanation with short paragraphs or bullet points.

CONCEPT / QUESTION FROM STUDENT:
\"\"\"
{concept}
\"\"\"

Now provide the simple explanation.
"""
    return prompt


def build_quiz_prompt(topic: str) -> str:
    """Prompt for the 'Generate Quiz' feature."""
    prompt = f"""You are a quiz-generation assistant helping a student practice
a topic before an exam.

TASK:
Create a multiple-choice quiz based on the study material or topic provided below.

REQUIREMENTS:
- Generate exactly 5 questions.
- Each question must have exactly 4 answer options labeled A, B, C, D.
- Only one option should be correct per question.
- Base every question directly on the supplied topic/content. Do not invent
  unrelated topics.
- After all 5 questions, provide a separate "Answer Key" section listing the
  correct option for each question (e.g., "1. B").

FORMAT EXACTLY LIKE THIS:

Question 1: <question text>
A) <option>
B) <option>
C) <option>
D) <option>

Question 2: <question text>
A) <option>
B) <option>
C) <option>
D) <option>

... (continue through Question 5)

Answer Key:
1. <correct letter>
2. <correct letter>
3. <correct letter>
4. <correct letter>
5. <correct letter>

STUDY MATERIAL / TOPIC:
\"\"\"
{topic}
\"\"\"

Now generate the quiz.
"""
    return prompt


def build_improve_answer_prompt(answer: str) -> str:
    """Prompt for the 'Improve My Answer' feature."""
    prompt = f"""You are a writing coach helping a student improve an exam or
assignment answer.

TASK:
Improve the clarity, structure, grammar, and completeness of the student's
answer below.

REQUIREMENTS:
- Do NOT replace the student's original idea or argument with a different one.
- Keep the core meaning and intent of the original answer.
- Fix grammar and awkward phrasing.
- Improve structure/flow if needed (e.g., splitting into clear points).
- Add missing detail only if it clearly strengthens the existing idea.
- After the improved answer, add a short "Feedback" section (2-4 bullet
  points) explaining what was changed and why.

FORMAT EXACTLY LIKE THIS:

Improved Answer:
<the improved version of the answer>

Feedback:
- <point 1>
- <point 2>
- <point 3>

STUDENT'S ORIGINAL ANSWER:
\"\"\"
{answer}
\"\"\"

Now provide the improved answer and feedback.
"""
    return prompt
