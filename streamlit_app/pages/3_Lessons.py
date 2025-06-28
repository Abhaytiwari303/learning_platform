import streamlit as st
from utils import fetch_lessons, add_lesson

st.title("📖 Lessons")

if "token" not in st.session_state:
    st.warning("Please login from the Login page.")
else:
    token = st.session_state['token']
    is_instructor = st.session_state.get("is_instructor", False)

    # Fetch lessons
    response = fetch_lessons(token)
    try:
        lessons = response.json()
        if isinstance(lessons, list):
            for l in lessons:
                st.markdown(f"**{l.get('title')}**\n{l.get('content')}")
        else:
            st.error("🚫 Error: " + str(lessons.get("detail", lessons)))
    except Exception as e:
        st.error(f"❌ Failed to load lessons: {e}")

    # Add lesson (Instructor only)
    if is_instructor:
        st.info(f"🔍 You are logged in as Instructor: {st.session_state.get('username')}")
        course_id = st.number_input("Course ID", min_value=1)
        title = st.text_input("Lesson Title")
        content = st.text_area("Lesson Content")


        if st.button("Create Lesson"):
            res = add_lesson(token, {"course": course_id, "title": title, "content": content})
            if res.status_code == 201:
                st.success("✅ Lesson added!")
                st.experimental_rerun()
            else:
                try:
                    st.error(f"❌ {res.json().get('detail', res.text)}")
                except:
                    st.error(f"❌ {res.text}")
    else:
        st.info("ℹ️ Only instructors can add lessons.")
