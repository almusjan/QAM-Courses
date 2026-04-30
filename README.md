# 🎓 QAM-Courses-CGP  
> **Quality Assurance & Management – Courses Platform**  
> *Graduation Project | Full-Stack Django Web Application*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Django](https://img.shields.io/badge/Django-4.2-0C4B33?logo=django)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.3-38B2AC?logo=tailwind-css)](https://tailwindcss.com/)
[![Deployed on Railway - expired free tier](https://img.shields.io/badge/Deployed%20on-Railway-0B0D0E?logo=railway)](https://railway.app)

A secure, scalable course management platform built as a **capstone graduation project**, enabling users to browse, favorite, and report educational sites/courses with role-based access control, email authentication, and cloud asset management.

---

## ✨ Features

### 🔐 User Management
- Secure registration & login with Django auth
- Email-based password reset with HTML templates
- User profile management with avatar upload (AWS S3)
- Session security & CSRF protection

### 📚 Course & Site Management
- Browse curated educational sites/courses
- Detailed site information pages with metadata
- **Favorite/Bookmark** functionality for personalized lists
- **Report system** for content moderation (user-submitted flags)

### 🎨 Modern UI/UX
- Fully responsive design with **Tailwind CSS 3.3**
- Themed UI via **FlyonUI** plugin (`corporate` & `dark` modes)
- Dynamic icons via **Iconify**
- Accessible, mobile-first components

### ☁️ Production-Ready Infrastructure
- **PostgreSQL** database (managed via Railway)
- **AWS S3** for static/media file storage
- **Whitenoise** + **Gunicorn** for efficient static serving & WSGI
- Environment-based configuration via `python-dotenv`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.11, Django 4.2 |
| **Frontend** | HTML5, Tailwind CSS 3.3, FlyonUI, Alpine.js (optional) |
| **Database** | PostgreSQL (Railway) |
| **Storage** | AWS S3 (via `django-storages` + `boto3`) |
| **Deployment** | Railway.app, Gunicorn, Whitenoise |
| **Auth** | Django Auth System, Email Backend |
| **Dev Tools** | `python-dotenv`, `black`, `flake8` (recommended) |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL (local or Railway)
- AWS S3 bucket (for production)
- [Railway CLI](https://docs.railway.app/guides/cli) (optional)

### 1. Clone & Install
```bash
git clone https://github.com/almusjan/QAM-Courses-CGP.git
cd QAM-Courses-CGP
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
