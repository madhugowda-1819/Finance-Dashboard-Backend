# Finance Dashboard Backend

A backend system for a Finance Dashboard where users interact with financial records based on their roles. Built with Django and Django REST Framework.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Project Architecture](#project-architecture)
- [Data Model](#data-model)
- [API Endpoints](#api-endpoints)
- [Access Control Logic](#access-control-logic)
- [Validation and Error Handling](#validation-and-error-handling)
- [Data Persistence](#data-persistence)
- [Optional Enhancements](#optional-enhancements)
- [Assumptions](#assumptions)
- [Setup Instructions](#setup-instructions)

---

## Project Overview

This project implements a backend system for a Finance Dashboard with the following capabilities:

- User management with role-based access
- Financial record CRUD operations
- Dashboard analytics and summaries
- Access control enforcement
- Input validation and error handling

---

## Technology Stack

| Layer | Technology |
|---|---|
| Backend Framework | Django |
| API Framework | Django REST Framework |
| Database | SQLite |
| Authentication | Session Authentication (Django default) |

---

## Project Architecture

The project is organized into three main apps:

```
finance_dashboard_backend
│
├── usersapp
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── permissions.py
│
├── recordsapp
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── dashboardapp
│   └── views.py
│
└── project settings
```

### App Responsibilities

| App | Responsibility |
|---|---|
| `usersapp` | User management and role permissions |
| `recordsapp` | Financial record CRUD operations |
| `dashboardapp` | Aggregated financial analytics |

---

## Data Model

### User Model

| Field | Description |
|---|---|
| `username` | Unique username |
| `email` | User email |
| `password` | Encrypted password |
| `role` | `viewer` / `analyst` / `admin` |
| `is_active` | User status |

#### Roles & Permissions

| Role | Permissions |
|---|---|
| Viewer | View dashboard only |
| Analyst | View records + dashboard insights |
| Admin | Manage users and financial records |

---

### FinancialRecord Model

| Field | Description |
|---|---|
| `user` | Linked user |
| `amount` | Transaction amount |
| `type` | `income` or `expense` |
| `category` | Transaction category |
| `date` | Transaction date |
| `notes` | Description |
| `created_at` | Record creation time |
| `is_deleted` | Soft delete flag |

#### Example Record

```
User:     madhu
Amount:   500
Type:     expense
Category: Food
Date:     2026-04-03
```

---

## API Endpoints

### User APIs

> Access: **Admin only**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/users/` | List all users |
| POST | `/api/users/` | Create a user |
| PUT | `/api/users/{id}/` | Update a user |
| DELETE | `/api/users/{id}/` | Delete a user |

---

### Financial Records APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/records/` | List records |
| POST | `/api/records/` | Create a record |
| PUT | `/api/records/{id}/` | Update a record |
| DELETE | `/api/records/{id}/` | Delete a record |

#### Filtering Examples

```
/api/records/?category=food
/api/records/?type=expense
/api/records/?date=2026-04-03
```

---

### Dashboard APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/dashboard/` | Summary analytics |

#### Response includes

- Total income
- Total expenses
- Net balance
- Category totals
- Recent transactions
- Monthly trends

#### Example Response

```json
{
  "total_income": 50000,
  "total_expense": 8000,
  "net_balance": 42000
}
```

---

## Access Control Logic

Role-based permissions are implemented using custom permission classes.

| Role | Dashboard | Records | Users |
|---|---|---|---|
| Viewer | ✅ View | ❌ | ❌ |
| Analyst | ✅ View | ✅ View | ❌ |
| Admin | ✅ Full | ✅ Full | ✅ Full |

Unauthorized operations return **`403 Forbidden`**.

---

## Validation and Error Handling

Input validation is implemented in serializers.

#### Validation Examples

| Field | Rule |
|---|---|
| `amount` | Must be greater than zero |
| `date` | Cannot be in the future |

#### HTTP Response Codes

| Code | Meaning |
|---|---|
| `200` | Success |
| `201` | Created |
| `400` | Invalid input |
| `403` | Permission denied |
| `404` | Resource not found |

---

## Data Persistence

- SQLite is used as the database.
- All financial records are stored in relational tables.
- **Soft delete** is implemented via `is_deleted = True` — deleted records are hidden but not permanently removed.

---

## Optional Enhancements

The following improvements are included in the project:

- Soft delete for financial records
- Role-based permissions
- Filtering financial records by category, type, and date
- Automatic user assignment for created records

---

## Assumptions

- Authentication uses Django session authentication.
- Each financial record belongs to one user.
- Analysts can only view records (no create/update/delete).
- Admin users manage all system data.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/madhugowda-1819/Finance-Dashboard-Backend.git
cd finance_dashboard_backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Create an admin user

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

The API will be accessible at:

```
http://127.0.0.1:8000/api/
```

---

## Conclusion

This backend demonstrates:

- Structured API design with Django REST Framework
- Role-based access control across all endpoints
- Financial data management with soft delete support
- Aggregated analytics via the dashboard API
- Robust input validation and error handling

The implementation focuses on clarity, maintainability, and logical architecture.
