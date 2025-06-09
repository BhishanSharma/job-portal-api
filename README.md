## 🧑‍💻 Mini Job Portal API

This is a backend API for a mini job portal built with Django and Django REST Framework. It supports user registration, employer job posting, and job applications with email notifications.

---

### 🚀 Tech Stack

* Python 3.x
* Django 5.x
* Django REST Framework
* SQLite (can be replaced with PostgreSQL)
* Token Authentication
* SMTP Email (Gmail)
* Swagger / ReDoc documentation

---

### 📁 Project Structure

```bash
project/
│
├── user_app/          # User registration & login
├── job_app/           # Job creation and listing (employers)
├── application_app/   # Job applications (normal users)
├── project/           # Core Django settings
├── manage.py
├── .env.example       # Sample environment variables
└── requirements.txt
```

---

### ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/job-portal-api.git
cd job-portal-api
```

2. **Create and Activate a Virtual Environment**

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Create `.env` File**

Copy the contents of `.env.example` and fill in your actual email credentials:

```bash
cp .env.example .env
```

5. **Apply Migrations**

```bash
python manage.py migrate
```

6. **Create Superuser (Optional)**

```bash
python manage.py createsuperuser
```

7. **Run the Server**

```bash
python manage.py runserver
```

---

### 🔐 Authentication

* Token-based authentication using `rest_framework.authtoken`.
* Get your token via `/api/token/login/` or `/api/token-auth/` (based on implementation).

---

### 📬 Email Notifications

Emails are sent:

* To applicants after applying to a job
* To job owners when someone applies

> SMTP is configured via environment variables.

---

### 📑 API Documentation

* Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

### 💼 Core Features

| Feature                     | Status |
| --------------------------- | ------ |
| User Registration/Login     | ✅ Done |
| Employer Job Posting (CRUD) | ✅ Done |
| Job Applications            | ✅ Done |
| Email Notifications         | ✅ Done |
| Signals (applicant count)   | ✅ Done |
| API Docs (Swagger/ReDoc)    | ✅ Done |
| Query Optimization          | ✅ Done |

---

### 📬 Sample .env Configuration

```env
SECRET_KEY='your-secret-key'
DEBUG=True

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='youremail@gmail.com'
EMAIL_HOST_PASSWORD='your-app-password'

DEFAULT_FROM_EMAIL='noreply@jobportal.com'
```

---

### 📮 Postman Collection (Optional)

You can export a Postman collection and share it here for testing endpoints. Ask if you'd like help creating one.
