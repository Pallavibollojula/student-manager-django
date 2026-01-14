<<<<<<< HEAD
# student-manager-django
=======
Super Pallavi 😄💙 then nee **current folder structure** (project-level `templates/` + `static/`) ki match ayye **final README.md** neat ga ichestha ✅
Copy paste into `README.md`

---

```md
# 🎓 Student Manager (Django + Templates + Static Files)

A clean and beginner-friendly Django project to manage student records using **Django Templates + SQLite Database**.  
This project also includes **Static Files setup (CSS + JavaScript)** for a neat UI.

---

## 🚀 Features

✅ Add Student  
✅ Update Student (using Roll Number)  
✅ Delete Student (using Roll Number)  
✅ View Student List (students page)  
✅ Django Admin Support  
✅ Static Files (CSS + JS) integrated  

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (db.sqlite3)

---

## 📂 Folder Structure (As in this project)

```

STUDENT_MANAGER/
│
├── student_manager/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── student_app/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── student_manager/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── students.html
│   │
│   ├── db.sqlite3
│   └── manage.py
│
└── venv/

````

---

## ⚙️ Setup & Run

### 1️⃣ Create Virtual Environment
```bash
py -m venv venv
````

### 2️⃣ Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 3️⃣ Install Django

```bash
pip install django
```

### 4️⃣ Run Migrations

```bash
py manage.py makemigrations
py manage.py migrate
```

### 5️⃣ Create Admin User (Optional)

```bash
py manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
py manage.py runserver
```

Open:
👉 [http://127.0.0.1:8000/student_app/](http://127.0.0.1:8000/student_app/)

---

## 🌐 Pages & URLs

### 🏠 Home Page

```
/student_app/
```

Contains:

* Add Student
* Update Student
* Delete Student

### 📋 Students Page

```
/student_app/students/
```

Contains:

* Student List

---

## 🧠 Student Model

```python
class Student(models.Model):
    full_name = models.CharField(max_length=60)
    age = models.IntegerField()
    roll_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.full_name
```

📌 `roll_number` is **unique**, so it is used for update and delete operations.

---

## 🔐 CSRF Token

All POST forms include:

```html
{% csrf_token %}
```

Without it Django will show:
❌ **403 Forbidden (CSRF verification failed)**

---

## 🎨 Static Files (CSS + JS)

Static files are used for styling and basic UI interaction.

### CSS load example:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### JS load example:

```html
<script src="{% static 'js/script.js' %}"></script>
```

---

## ⚡ JavaScript Usage

JavaScript is used for UI actions like toggling sections.

Example:

```js
document.addEventListener("DOMContentLoaded", () => {
  const studentsLink = document.getElementById("studentsLink");
  const studentListCard = document.getElementById("studentListCard");

  if (!studentsLink || !studentListCard) return;

  studentsLink.addEventListener("click", (e) => {
    e.preventDefault();
    studentListCard.classList.toggle("show");
  });
});
```

---

## 🛡️ Common Errors & Fixes

### ❌ TemplateDoesNotExist

✅ Fix: Make sure templates are inside:

```
student_manager/templates/
```

and `settings.py` has template DIR configured.

### ❌ IntegrityError (UNIQUE constraint failed)

✅ Fix: Roll Number must be unique.
Use a new roll number for each student.

### ❌ Page not found (404)

✅ Fix: Check URL patterns in `student_app/urls.py`

---

## 🌟 Future Improvements (Optional)

✅ Search student by roll number
✅ Add delete button inside student list
✅ Add success/error messages using Django Messages
✅ Authentication (Login/Logout)
✅ Convert to REST API (Django REST Framework)

---

## 👩‍💻 Author

Built with 💙 by **Pallavi**
Django Practice Project 🚀

```


>>>>>>> 3974bcb (Student Manager project)
