import streamlit as st
from utils import fetch_courses, add_course

st.title("📘 Courses")

if "token" not in st.session_state:
    st.warning("Please login from the Login page.")
else:
    token = st.session_state["token"]
    is_instructor = st.session_state.get("is_instructor", False)

    # Fetch and show courses
    response = fetch_courses(token)
    try:
        courses = response.json()
        if isinstance(courses, list):
            st.subheader("📚 Available Courses")
            for c in courses:
                st.markdown(f"### {c.get('title')}\n{c.get('description')}")
        else:
            st.error("🚫 Error: " + str(courses.get("detail", courses)))
    except Exception as e:
        st.error(f"❌ Failed to load courses: {e}")

    # Instructor-only course creation
    if is_instructor:
        st.subheader("➕ Add a New Course")
        title = st.text_input("Course Title")
        desc = st.text_area("Course Description")

        if st.button("Create Course"):
            data = {"title": title, "description": desc}
            res = add_course(token, data)

            try:
                result = res.json()
            except:
                result = {"detail": res.text}

            if res.status_code == 201:
                st.success("✅ Course created!")
                st.experimental_rerun()
            else:
                st.error(f"❌ Failed: {result.get('detail', result)}")
    else:
        st.info("ℹ️ Only instructors can create courses.")
