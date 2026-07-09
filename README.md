# Expense Manager Pro - Backend

A modern RESTful Expense Management API built with **FastAPI**, **SQLAlchemy**, **JWT Authentication**, and **PostgreSQL/SQLite**.

This backend provides secure authentication, expense management, category management, analytics, reports, and export functionality.

---

# Features

- User Registration
- JWT Authentication
- Secure Password Hashing (bcrypt)
- Expense CRUD Operations
- Category CRUD Operations
- Dashboard Statistics
- Expense Analytics
- Monthly Reports
- Yearly Reports
- Category Reports
- CSV Export
- Excel Export
- Swagger API Documentation
- Alembic Database Migrations

---

# Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy ORM
- Alembic
- PostgreSQL / SQLite
- Pydantic
- JWT Authentication
- Passlib (bcrypt)
- Uvicorn

---

# Project Structure

```
app/
│
├── api/
│   └── v1/
│       ├── auth.py
│       ├── expenses.py
│       ├── categories.py
│       ├── analytics.py
│       ├── dashboard.py
│       ├── report.py
│       └── export.py
│
├── core/
├── db/
├── dependencies/
├── models/
├── schemas/
├── services/
├── utils/
│
main.py
```

---

# API Endpoints

## Authentication

| Method | Endpoint |
|----------|----------------|
| POST | /auth/register |
| POST | /auth/login |

---

## Categories

| Method | Endpoint |
|----------|----------------|
| GET | /categories |
| POST | /categories |
| PUT | /categories/{id} |
| DELETE | /categories/{id} |

---

## Expenses

| Method | Endpoint |
|----------|----------------|
| GET | /expenses |
| POST | /expenses |
| PUT | /expenses/{id} |
| DELETE | /expenses/{id} |

---

## Dashboard

| Method | Endpoint |
|----------|----------------|
| GET | /dashboard |

Returns

- Total Expenses
- Today's Expenses
- Weekly Expenses
- Monthly Expenses
- Highest Expense
- Total Categories

---

## Analytics

| Method | Endpoint |
|----------|----------------|
| GET | /analytics/monthly |
| GET | /analytics/category |

---

## Reports

| Method | Endpoint |
|----------|----------------|
| GET | /reports/monthly |
| GET | /reports/yearly |
| GET | /reports/category |

---

## Export

| Method | Endpoint |
|----------|----------------|
| GET | /export/csv |
| GET | /export/excel |

---

# Installation

Clone repository

```bash
git clone https://github.com/yourusername/expense-manager-backend.git
```

Move into project

```bash
cd expense-manager-backend
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env`

```
DATABASE_URL=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Database Migration

```bash
alembic revision --autogenerate -m "Initial"
alembic upgrade head
```

---

# Run Server

```bash
uvicorn main:app --reload
```

API

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Authentication

Uses JWT Bearer Authentication.

After login:

```
Authorization:
Bearer <access_token>
```

---

# Built With

- FastAPI
- SQLAlchemy
- Alembic
- JWT
- PostgreSQL
- Pydantic

---

# Author

Syeda Sidra Sherazi
