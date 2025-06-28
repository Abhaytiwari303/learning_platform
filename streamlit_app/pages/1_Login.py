import streamlit as st
import requests
from utils import register_user, login_user, get_headers

st.title("🔐 Login or Register")

choice = st.radio("Choose action", ["Login", "Register"])

API_BASE = "http://127.0.0.1:8000/api/"

if choice == "Register":
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    is_student = st.checkbox("Register as Student", value=True)

    if st.button("Register"):
        data = {
            "username": username,
            "email": email,
            "password": password,
            "is_student": is_student,
            "is_instructor": not is_student
        }

        res = register_user(data)
        if res.status_code == 201:
            st.success("✅ Registered successfully! Please login.")
        else:
            try:
                st.error(f"❌ Registration failed: {res.json().get('detail', res.json())}")
            except:
                st.error(f"❌ Registration failed: {res.text}")

else:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        data = {"username": username, "password": password}
        res = login_user(data)

        if res.status_code == 200:
            token = res.json().get('access')
            st.session_state['token'] = token
            st.session_state['username'] = username

            # ✅ Fetch user roles from /accounts/me/
            try:
                user_res = requests.get(API_BASE + "accounts/me/", headers=get_headers(token))
                
                # ✅ Debug logs
                st.text(f"Status Code: {user_res.status_code}")
                st.text(f"Response Text: {user_res.text}")
                
                user_data = user_res.json()
                
                st.session_state["is_instructor"] = user_data.get("is_instructor", False)
                st.session_state["is_student"] = user_data.get("is_student", False)
                
                st.success(f"✅ Logged in as {username}")
                st.info(f"👤 Role: {'Instructor' if st.session_state['is_instructor'] else 'Student'}")
            except Exception as e:
                st.error("✅ Login succeeded but failed to fetch role info.")
                st.text(str(e))


        else:
            try:
                st.error(f"❌ Login failed: {res.json().get('detail', res.json())}")
            except:
                st.error(f"❌ Login failed: {res.text}")
