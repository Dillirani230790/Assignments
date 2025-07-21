import streamlit as st

# Page setup
st.set_page_config(page_title="Quiz App", page_icon="🧠", layout="centered")

# Quiz questions
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["Albert Einstein", "Nikola Tesla", "Thomas Edison", "Isaac Newton"],
        "answer": "Thomas Edison"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Hydrogen", "Nitrogen", "Carbon Dioxide"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    }
]

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []
if "selected" not in st.session_state:
    st.session_state.selected = None

st.title("🧠 General Knowledge Quiz")

# Quiz in progress
if st.session_state.q_index < len(quiz):
    q = quiz[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index + 1}: {q['question']}")

    selected = st.radio("Choose your answer:", q["options"], index=0, key=st.session_state.q_index)
    st.session_state.selected = selected

    if st.button("Next"):
        if st.session_state.selected == q["answer"]:
            st.success("Correct! ✅")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect ❌. Correct answer: {q['answer']}")
            st.session_state.wrong_answers.append({
                "question": q["question"],
                "your_answer": st.session_state.selected,
                "correct_answer": q["answer"]
            })

        st.session_state.q_index += 1
        st.rerun()

# Quiz completed
else:
    st.success(f"🎉 Quiz completed! Your score: {st.session_state.score} / {len(quiz)}")

    if st.session_state.wrong_answers:
        st.markdown("### ❌ Here's what you missed:")
        for wa in st.session_state.wrong_answers:
            st.markdown(f"""
            **Q:** {wa['question']}  
            - Your Answer: ❌ *{wa['your_answer']}*  
            - Correct Answer: ✅ **{wa['correct_answer']}**
            """, unsafe_allow_html=True)
    else:
        st.balloons()
        st.success("Fantastic! All answers correct! 🎯")

    if st.button("Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.wrong_answers = []
        st.session_state.selected = None
        st.rerun()
