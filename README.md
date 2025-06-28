# 🎓 Online Learning Platform

An end-to-end web application for course management, lesson creation, quiz administration, and student progress tracking. Built with **Django**, **DRF**, **Channels**, and **Streamlit**.

---

## 🚀 Features

### 👩‍🏫 Admin / Instructor
- Create and manage **Courses**
- Add **Lessons** under each course
- Create **Quizzes** for lessons
- Track **Student Submissions**

### 👨‍🎓 Student
- View available **Courses** and **Lessons**
- Attempt **Quizzes**
- See quiz results and correctness

### 📡 Real-Time
- Notification support with Django **Channels + Redis**

---

## 🛠 Tech Stack

| Backend        | Frontend   | Database         | Real-time           |
|----------------|------------|------------------|---------------------|
| Django + DRF   | Streamlit  | PostgreSQL/SQLite | Django Channels + Redis |

---

## 🧾 API Endpoints

POST /api/accounts/register/ # Register users
POST /api/token/ # JWT login
GET /api/accounts/me/ # Get current user info
GET /api/courses/ # List all courses
POST /api/courses/ # Create a course
GET /api/lessons/ # List all lessons
POST /api/lessons/ # Create a lesson
GET /api/quizzes/quizzes/ # List quizzes
POST /api/quizzes/quizzes/ # Create a quiz
POST /api/quizzes/submit/<id>/ # Submit quiz answer
GET /api/quizzes/submissions/ # View quiz submissions


---

## 🖥️ Streamlit Interface Pages

- 🔐 **Login / Register**
- 📘 **Courses** – View & create (for instructors)
- 📖 **Lessons** – View & create (for instructors)
- ❓ **Quizzes** – Attempt and submit answers
- 📊 **Student Quiz Submissions** – View past attempts and results

---

## ⚙️ Setup Instructions

### ✅ Backend Setup


git clone https://github.com/Abhaytiwari303/learning_platform.git
cd learning_platform

# Create and activate virtual environment
python -m venv learning_platform_env
source learning_platform_env/bin/activate  # On Windows: .\learning_platform_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations and start server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
✅ Frontend Setup (Streamlit)

cd streamlit_app
streamlit run app.py

### 📁 Project Structure

learning_platform/
├── accounts/           # User registration & roles
├── courses/            # Course models & views
├── lessons/            # Lesson models & views
├── quizzes/            # Quiz & submission logic
├── notifications/      # Real-time events
├── streamlit_app/
│   ├── app.py
│   └── pages/          # All Streamlit subpages
└── manage.py
🔒 Environment Setup (.env)
Your .env file should be kept secret and excluded from Git using .gitignore.


DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
REDIS_URL=redis://localhost:6379
Add this to .gitignore:

.env
✨ Future Improvements
👤 User Profile Dashboard

🏆 Leaderboards

🎓 Course Completion Certificates

📎 File/Assignment Uploads

🔔 Push Notifications

👨‍💻 Developer
Abhay Tiwari


### Screenshot
![Screenshot 2025-06-28 225044](https://github.com/user-attachments/assets/29d0b570-cbff-4d6f-bd7c-f011debbb809)
![Screenshot 2025-06-28 225036](https://github.com/user-attachments/assets/3c747b06-bf78-4ba6-9ad0-0392869b7e4e)
![Screenshot 2025-06-28 225028](https://github.com/user-attachments/assets/cf1ccd40-c7b9-43ab-9adf-ea8d464830ba)
![Screenshot 2025-06-28 225020](https://github.com/user-attachments/assets/178a3db0-f007-4039-b0b8-44175af8ed65)
![Screenshot 2025-06-28 225011](https://github.com/user-attachments/assets/11a6d0ca-4648-4ca8-852b-550879cd82e9)
![Screenshot 2025-06-28 225053](https://github.com/user-attachments/assets/8c1a1e12-b394-47cd-8b03-a5e5c1331637)






