import streamlit as st
from utils import fetch_quizzes, submit_answer

st.title("❓ Quizzes")

if "token" not in st.session_state:
    st.warning("Please login from the Login page.")
else:
    token = st.session_state["token"]

    response = fetch_quizzes(token)

    st.code(response.text)  # 👈 Show raw response

    try:
        quizzes = response.json()

        if isinstance(quizzes, list):
            if not quizzes:
                st.info("📭 No quizzes available.")
            for quiz in quizzes:
                st.subheader(f"Q: {quiz.get('question')}")
                answer = st.text_input(f"Your answer for quiz #{quiz.get('id')}", key=f"answer_{quiz.get('id')}")

                if st.button("Submit", key=f"submit_{quiz.get('id')}"):
                    res = submit_answer(token, quiz.get("id"), answer)

                    try:
                        res_data = res.json()
                        if res.status_code == 201:
                            st.success("✅ Submission successful!")
                            st.info(f"Result: {res_data.get('result')}")
                        else:
                            st.error(f"❌ {res_data.get('detail', res.text)}")
                    except Exception as e:
                        st.error(f"❌ Unexpected error: {e}")
                        st.text(f"Response content: {res.text}")

        else:
            st.error(f"🚫 Error: Expected a list but got: {type(quizzes)}")
    except Exception as e:
        st.error(f"❌ Failed to fetch quizzes: {e}")
