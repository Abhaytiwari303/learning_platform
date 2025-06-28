import requests

API_BASE = "http://127.0.0.1:8000/api/"
def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


def fetch_courses(token):
    return requests.get(API_BASE + "courses/", headers=get_headers(token))

def add_course(token, data):
    return requests.post(API_BASE + "courses/", json=data, headers=get_headers(token))

def fetch_lessons(token):
    return requests.get(API_BASE + "lessons/", headers=get_headers(token))

def add_lesson(token, data):
    return requests.post(API_BASE + "lessons/", json=data, headers=get_headers(token))

def fetch_quizzes(token):
    url = "http://127.0.0.1:8000/api/quizzes/quizzes/" 
    return requests.get(url, headers=get_headers(token))


def submit_answer(token, quiz_id, answer):
    url = f"http://127.0.0.1:8000/api/quizzes/submit/{quiz_id}/"  # ✅ Fixed
    data = {"answer": answer}
    return requests.post(url, headers=get_headers(token), json=data)


def register_user(data):
    return requests.post(API_BASE + "accounts/register/", json=data)

def login_user(data):
    return requests.post(API_BASE + "token/", json=data)
