import streamlit as st
import random

st.set_page_config(page_title="🧠 Logical Reasoning Quiz", layout="centered")
st.title("🧩 Logical Reasoning Quiz")

# All available puzzles
all_puzzles = [
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", ["echo"]),
    ("The more you take, the more you leave behind. What are they?", ["footsteps", "steps"]),
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", ["m", "the letter m", "letter m"]),
    ("Forward I am heavy, but backward I am not. What am I?", ["ton"]),
    ("A man is looking at a photograph. He says: 'Brothers and sisters, I have none. That man's father is my father's son.' Who is in the photograph?", ["son", "his son", "the man's son"]),
    ("What has keys but can't open locks?", ["piano"]),
    ("What has hands but can’t clap?", ["clock"]),
    ("What begins with T, ends with T, and has T in it?", ["teapot"]),
    ("What has to be broken before you can use it?", ["egg"]),
    ("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", ["map"]),
]

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.questions = random.sample(all_puzzles, 5)  # pick 5 random puzzles

# Get current question
index = st.session_state.index

if index < len(st.session_state.questions):
    question, correct_answers = st.session_state.questions[index]
    st.subheader(f"Question {index + 1} of {len(st.session_state.questions)}")
    st.markdown(f"**{question}**")

    user_input = st.text_input("Your Answer:", key=f"q{index}")

    if st.button("Submit", key=f"submit{index}"):
        user_clean = user_input.strip().lower()
        is_correct = user_clean in [ans.lower() for ans in correct_answers]

        if is_correct:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer: **{correct_answers[0].capitalize()}**")

        # Store result
        st.session_state.answers.append({
            "question": question,
            "your_answer": user_input.strip(),
            "correct": is_correct,
            "correct_answer": correct_answers[0]
        })

        st.session_state.index += 1
        st.rerun()

else:
    # Quiz done
    st.success(f"🎉 Quiz Completed! Your Score: {st.session_state.score} / {len(st.session_state.questions)}")
    st.markdown("### 📋 Review Your Answers:")
    for i, ans in enumerate(st.session_state.answers, 1):
        st.markdown(f"**Q{i}:** {ans['question']}")
        if ans['correct']:
            st.success(f"✅ Your Answer: {ans['your_answer']}")
        else:
            st.error(f"❌ Your Answer: {ans['your_answer']}  \n✅ Correct Answer: {ans['correct_answer'].capitalize()}")
        st.markdown("---")

    if st.button("🔁 Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
