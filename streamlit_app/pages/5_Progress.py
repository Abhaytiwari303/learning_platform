import streamlit as st
import requests
from utils import get_headers

st.title("📊 Student Quiz Submissions")

if "token" not in st.session_state:
    st.warning("Please login.")
else:
    res = requests.get(
        "http://127.0.0.1:8000/api/quizzes/submissions/",  # ✅ Corrected path
        headers=get_headers(st.session_state["token"])
    )

    if res.status_code == 200:
        try:
            data = res.json()
            if not data:
                st.info("No submissions found.")
            for item in data:
                st.markdown(f"👤 **User ID:** {item['user']}")
                st.markdown(f"📌 Quiz ID: {item['quiz']}")
                st.markdown(f"📝 Answer: `{item['submitted_answer']}`")
                st.markdown(f"✅ Correct: {'Yes' if item['correct'] else 'No'}")
                st.markdown("---")
        except Exception as e:
            st.error(f"❌ Failed to parse response: {e}")
    else:
        st.error(f"🚫 Failed to fetch submissions: {res.status_code}\n\n{res.text}")
