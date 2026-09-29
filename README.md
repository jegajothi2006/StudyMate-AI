# StudyMate AI 🎓

**StudyMate AI** is an AI-powered student productivity application developed using Python and Streamlit as part of the **ShadowFox AI Engineer Internship – Beginner Level, Task 1**.

The application uses the Google Gemini API to help students with common academic tasks, including summarizing notes, understanding concepts, generating quizzes, and improving written answers.

---

## 📌 Project Overview

Students often spend considerable time summarizing lengthy notes, understanding difficult concepts, preparing for tests, and improving written answers.

StudyMate AI provides four focused AI-powered utilities in a simple, user-friendly web application. It helps students complete these tasks more efficiently without requiring them to write their own AI prompts.

## 🎯 Objectives

- Simplify everyday academic tasks using AI.
- Help students understand complex concepts through clear explanations.
- Generate practice quizzes for self-assessment.
- Improve the grammar, clarity, and structure of written answers.
- Demonstrate the practical use of Python, Streamlit, prompt engineering, and the Google Gemini API.

---

## ✨ Features

### 1. Summarize Notes
Converts lengthy study notes into concise, structured summaries. This helps students review important information more efficiently.

### 2. Explain a Concept
Provides simple, student-friendly explanations of difficult concepts, along with examples to support understanding.

### 3. Generate Quiz
Creates **5 multiple-choice questions (MCQs)** based on a given topic or study material. Each question includes four options and a separate answer key.

### 4. Improve My Answer
Improves a student's written answer by correcting grammar and enhancing clarity and structure while preserving the original meaning. It also provides feedback on the answer.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Streamlit | Web application interface |
| Google Gemini API | Generates AI-powered responses |
| python-dotenv | Loads environment variables from a local `.env` file |
| Git and GitHub | Version control and project hosting |

---

## 🏗️ Project Structure

```text
StudyMate-AI/
│
├── app.py              # Main Streamlit application
├── prompts.py          # Prompt-building functions for each utility
├── requirements.txt    # Required Python packages
├── .env.example        # Example environment configuration
├── .gitignore          # Excludes sensitive and unnecessary files
└── README.md           # Project documentation
```

**Note:** The actual `.env` file containing your API key should be created locally. It should never be uploaded to GitHub.

---

## ⚙️ How It Works

1. The user opens the StudyMate AI application.
2. The user selects one of the four utilities from the sidebar.
3. The user enters or pastes the required text or topic.
4. The application validates the input to ensure it is suitable for processing.
5. A task-specific prompt is generated using functions defined in `prompts.py`.
6. The prompt is sent to the Google Gemini API using the configured model.
7. The application displays the generated response in a readable format.
8. If an error occurs, the application displays a user-friendly error message.

---

## 🚀 Installation and Setup

Follow these steps to run StudyMate AI on your local machine.

### Prerequisites

Make sure you have installed:

- Python 3
- pip
- Git (optional, for cloning the repository)
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/jegajothi2006/StudyMate-AI.git
```

Navigate to the project directory:

```bash
cd StudyMate-AI
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 5. Configure the API Key

Create a `.env` file in the project directory.

You can copy the example file on Windows:

```bash
copy .env.example .env
```

Open the `.env` file and add your Google Gemini API key:

```env
LLM_API_KEY=your_gemini_api_key_here
LLM_MODEL=gemini-3.5-flash-lite
```

Replace `your_gemini_api_key_here` with your actual API key.

**Important:** Keep your API key private. Never commit or upload your `.env` file to GitHub.

### 6. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default browser. If it does not, open:

```text
http://localhost:8501
```

---

## 💡 Example Usage

### Example 1: Explain a Concept

**Input:**

```text
What is recursion in programming?
```

**Expected Output:**

A simple explanation of recursion, describing how a function calls itself, along with an example such as calculating a factorial.

### Example 2: Generate Quiz

**Input:**

```text
Photosynthesis
```

**Expected Output:**

Five multiple-choice questions about photosynthesis, each with four options, followed by a separate answer key.

---

## 🛡️ Error Handling

StudyMate AI includes error handling to provide a better user experience.

- **Empty Input:** Displays a message asking the user to enter content.
- **Short Input:** Requests additional content when the input is too short.
- **Missing or Invalid API Key:** Displays an appropriate authentication error.
- **Network Errors:** Informs the user if the application cannot connect to the API.
- **Rate Limits:** Displays a message when the API request limit is reached.
- **Unexpected Errors:** Shows a friendly error message instead of exposing a Python traceback.

---

## 🧠 Prompt Engineering

Prompt engineering is an important part of StudyMate AI.

Each utility has its own prompt-building function in `prompts.py`. Instead of using one general prompt for every task, the application uses specific instructions tailored to each utility.

The prompts define:

- **Role:** The role the AI should perform, such as a tutor or writing assistant.
- **Task:** The specific action the AI should complete.
- **Input:** The student's content or question.
- **Output Format:** The expected structure and presentation of the response.

For example, the quiz-generation prompt requests exactly five multiple-choice questions, four options per question, and a separate answer key.

This approach helps make the AI's responses more relevant to each task.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Python application development.
- Building interactive web applications using Streamlit.
- Integrating the Google Gemini API.
- Using environment variables to protect API keys.
- Writing task-specific prompts.
- Implementing input validation and error handling.
- Organizing a Python project into multiple files.
- Using GitHub to manage and share project code.

---

## 🔮 Future Improvements

Possible future enhancements include:

- Uploading PDF and text files for note summarization.
- Allowing users to customize quiz difficulty and question count.
- Adding options to download summaries and quizzes.
- Maintaining a history of previous responses.
- Supporting multiple large language model providers.

---

## 📌 Project Scope

StudyMate AI was developed as a beginner-level internship project.

It is a simple, single-application system focused on four academic utilities. It uses the Google Gemini API to generate responses and does not require a separate backend server or database.

The project does not currently implement Retrieval-Augmented Generation (RAG), vector databases, or AI agents.

---

## 👩‍💻 Developed By

**Jegajothi K**  
B.Tech – Information Technology  
Manakula Vinayagar Institute of Technology  

**Internship:** ShadowFox AI Engineer Internship  
**Level:** Beginner  
**Task:** Task 1 – StudyMate AI

---

## 📄 License

This project was developed for educational and internship purposes.
