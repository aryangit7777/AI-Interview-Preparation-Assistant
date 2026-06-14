# 🤖 AI Interview Preparation Assistant

An AI-powered interview preparation platform built using **Python, Streamlit, and Google Gemini API**. The application helps users practice technical interviews by generating role-specific interview questions, evaluating responses, and maintaining interview history.

## 🚀 Features

### 🎯 Role-Based Interview Questions

Generate interview questions for different technical roles:

* AI Engineer
* Python Developer
* Data Analyst
* Full Stack Developer

### 🧠 AI-Powered Answer Evaluation

The application evaluates candidate responses and provides:

* Score out of 10
* Strengths
* Areas for Improvement
* Suggested Correct Answer

### 💾 Interview Memory

Stores interview attempts in a JSON file and allows users to review previous sessions.

### 🎨 User-Friendly Interface

Built with Streamlit for an interactive and easy-to-use experience.

### ⚠️ Error Handling

Handles API rate limits and runtime errors gracefully.

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini API (Gemini 2.5 Flash)

### Storage

* JSON

### Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
AI_Interview_Preparation_Assistant/
│
├── app.py
├── history.json
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── secrets.toml
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/aryangit7777/AI-Interview-Preparation-Assistant.git
cd AI-Interview-Preparation-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a file:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📊 Application Workflow

1. Select a target role.
2. Generate an interview question.
3. Enter your answer.
4. Receive AI-generated feedback.
5. Store interview history.
6. Review previous interview attempts.

---

## 📸 Screenshots

Add screenshots here:

* Home Page
* Generated Question
* AI Feedback
* Interview History

---

## 🔮 Future Enhancements

* Difficulty Levels (Beginner, Intermediate, Advanced)
* Progress Dashboard
* PDF Report Generation
* Authentication System
* Additional Interview Domains
* Performance Analytics

---

## 🎓 Learning Outcomes

This project helped me learn:

* Generative AI Application Development
* Gemini API Integration
* Streamlit Application Development
* Prompt Engineering
* Session State Management
* JSON Data Handling
* Git & GitHub Workflow
* Error Handling and Debugging

---

## 👨‍💻 Author

**Aryan**

Aspiring AI & Generative AI Engineer

GitHub: https://github.com/aryangit7777
