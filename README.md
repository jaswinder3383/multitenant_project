# multitenant_project

# Django Multi-Tenant System

This is a multi-tenant SaaS system built using Django, DRF, Celery, and Redis. It supports:
- Subdomain-based tenants
- Plan & feature management
- Usage-based billing via email (powered by Celery)
- JWT-based login for tenant users

---

## 🚀 Features

- Superadmin can:
  - Create tenants
  - Create subscription plans and features
  - Assign features to plans
  - Trigger billing emails (based on feature usage)
- Tenants can:
  - Select plans
  - Create their own users
  - Use features (which increases usage count)
- Celery and Redis used for background tasks (e.g., billing emails)

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 5+
- Django Rest Framework
- PostgreSQL / MySQL
- Redis
- Celery
- drf-yasg (Swagger for API docs)
- SimpleJWT

---

## 🧩 Project Setup Instructions

### 🔧 1. Clone the Repo
```bash
git clone https://github.com/jaswinder3383/multitenant_project.git
cd multitenant_project  

📦 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate          # On Windows
 3. Install Dependencies
pip install -r requirements.txt
Database Setup

python manage.py createsuperuser
Run Development Server

python manage.py runserver


