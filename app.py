import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

if "question" not in st.session_state:
    st.session_state.question = ""


def load_history():
    try:
        with open("history.json", "r") as file:
            return json.load(file)
    except:
        return []


def save_history(history):
    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)


st.set_page_config(page_title="AI Interview Assistant", page_icon="🤖", layout="wide")

st.title("🤖 AI Interview Preparation Assistant")
st.markdown(
    "Practice interviews, receive AI-powered feedback, and track your progress."
)

with st.sidebar:
    st.header("📌 Project Info")

    st.write("AI Interview Preparation Assistant")

    st.write("Tech Stack:")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Gemini API")
    st.write("- JSON Memory")

    st.success("Ready for Interview Practice 🚀")

role = st.selectbox(
    "💼 Select Target Role",
    ["AI Engineer", "Python Developer", "Data Analyst", "Full Stack Developer"],
)

# Generate Question
if st.button("🎯 Generate Question"):

    prompt = f"""
    Generate ONE beginner-level interview question
    for a {role}.

    Return only the question.
    """

    response = model.generate_content(prompt)

    st.session_state.question = response.text

# Show Question
if st.session_state.question:

    st.subheader("❓ Interview Question")
    st.info(st.session_state.question)

    answer = st.text_area("Enter your answer:", height=150)

    if st.button("📝 Evaluate Answer"):

        evaluation_prompt = f"""
        You are an interview evaluator.

        Role: {role}

        Question:
        {st.session_state.question}

        Candidate Answer:
        {answer}

        Evaluate the answer and provide:

        1. Score out of 10
        2. Strengths
        3. Areas of Improvement
        4. Correct Answer
        """

        try:
            evaluation = model.generate_content(evaluation_prompt)

            history = load_history()
            history.append(
                {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "role": role,
                    "question": st.session_state.question,
                    "answer": answer,
                }
            )

            save_history(history)

            st.subheader("AI Feedback")
            st.write(evaluation.text)

        except Exception:
            st.error("Gemini rate limit reached. Please wait a minute and try again.")

st.divider()

st.subheader("📜 Recent Interview History")

history = load_history()

if history:

    for item in reversed(history[-5:]):

        with st.expander(f"{item['role']} | {item['date']}"):
            st.write("Question:")
            st.write(item["question"])

else:
    st.info("No interview history yet.")
