# 🎓 Student Manager (Django CRUD)

A clean and beginner-friendly Django project to manage student records using **Django Templates + SQLite Database**.  
This project also includes **Static Files setup (CSS + JavaScript)** for a neat and responsive UI.

---

## 🚀 Features

- ✅ Add Student  
- ✅ Update Student (using Roll Number)  
- ✅ Delete Student (using Roll Number)  
- ✅ View Student List (Students page)  
- ✅ Django Admin Support  
- ✅ Static Files (CSS + JS) integrated  

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite  

---

## 📂 Folder Structure

```text
STUDENT_MANAGER/
├── student_manager/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │
│   ├── student_app/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── student_manager/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── students.html
│   │
│   ├── db.sqlite3
│   └── manage.py
│
└── venv/
⚙️ Setup & Run
1) Create virtual environment
bash
Copy code
py -m venv venv
2) Activate virtual environment
bash
Copy code
venv\Scripts\activate
3) Install Django
bash
Copy code
pip install django
4) Run migrations
bash
Copy code
py manage.py makemigrations
py manage.py migrate
5) Create superuser (Optional)
bash
Copy code
py manage.py createsuperuser
6) Run server
bash
Copy code
py manage.py runserver
Open in browser:
👉 http://127.0.0.1:8000/student_app/

🌐 Pages & URLs
🏠 Home Page
/student_app/

Contains:

Add Student

Update Student

Delete Student

📋 Students Page
/student_app/students/

Contains:

Student List

🧠 Student Model
python
Copy code
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=60)
    age = models.IntegerField()
    roll_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.full_name
📌 roll_number is unique, so it is used for update and delete operations.

🔐 CSRF Token
All POST forms include:

html
Copy code
{% csrf_token %}
Without this Django shows:

❌ 403 Forbidden (CSRF verification failed)

🎨 Static Files
CSS load:

html
Copy code
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
JS load:

html
Copy code
<script src="{% static 'js/script.js' %}"></script>
⚡ JavaScript
JavaScript is used for UI actions like toggling sections.

js
Copy code
document.addEventListener("DOMContentLoaded", () => {
  const studentsLink = document.getElementById("studentsLink");
  const studentListCard = document.getElementById("studentListCard");

  if (!studentsLink || !studentListCard) return;

  studentsLink.addEventListener("click", (e) => {
    e.preventDefault();
    studentListCard.classList.toggle("show");
  });
});
🛡️ Common Errors & Fixes
❌ TemplateDoesNotExist
✅ Fix: Make sure templates are inside templates/ folder and settings.py has correct template DIR config.

❌ IntegrityError (UNIQUE constraint failed)
✅ Fix: roll_number must be unique. Use a new roll number for each student.

❌ Page not found (404)
✅ Fix: Check URL patterns in student_app/urls.py

🌟 Future Improvements (Optional)
✅ Search student by roll number

✅ Add delete button inside student list

✅ Add success/error messages using Django Messages

✅ Authentication (Login/Logout)

✅ Convert to REST API (Django REST Framework)

👩‍💻 Author
Built with 💙 by Pallavi
Django Practice Project 🚀
