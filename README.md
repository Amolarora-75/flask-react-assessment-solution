# 🧠 Flask + React Fullstack Assessment  

> A complete end-to-end Task Management and Commenting System built using **Flask (Python)** and **React (Vite)**.  
> This project demonstrates a simple full-stack workflow with RESTful APIs, database integration, testing, and responsive frontend UI.

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Backend Setup (Flask)](#backend-setup-flask)
6. [Frontend Setup (React)](#frontend-setup-react)
7. [Running Tests](#running-tests)
8. [API Endpoints](#api-endpoints)
9. [Pull Request Guidelines](#pull-request-guidelines)
10. [Contributors](#contributors)

---

## 🧩 Overview
This project was developed as part of a **Fullstack Software Engineer Assessment**.  
It consists of a **Flask backend** that handles RESTful APIs for tasks and comments, and a **React frontend** that allows users to interact with those APIs via a modern UI.

---

## ⚙️ Tech Stack

### **Backend**
- Python 3.10+
- Flask 3.x
- Flask-CORS
- SQLAlchemy
- Pytest

### **Frontend**
- React 18 (Vite)
- JavaScript (ES6+)
- Fetch API

---

## ✨ Features
- CRUD operations for **Tasks**
- CRUD operations for **Comments** (linked to tasks)
- Clean RESTful API structure
- Pytest-based automated backend testing
- Lightweight and responsive React UI
- Proxy configuration for API routing between frontend and backend

---

## 📁 Project Structure
fullstack-assessment/
│
├── backend/
│ ├── app.py # Flask entry point
│ ├── database.py # SQLAlchemy setup
│ ├── models.py # Task & Comment models
│ ├── routes.py # API endpoints
│ ├── tests/
│ │ └── test_comments.py # Pytest cases for CRUD
│ ├── requirements.txt
│ └── init.py
│
├── frontend/
│ ├── src/
│ │ ├── main.jsx
│ │ ├── App.jsx
│ │ └── pages/Tasks.jsx
│ ├── vite.config.js
│ ├── package.json
│ └── index.html
│
└── README.md


---

## 🧰 Backend Setup (Flask)

### 1️⃣ Create a virtual environment
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate     # Windows
# or
source .venv/bin/activate  # macOS/Linux

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask server
python app.py


✅ The backend runs at:

http://localhost:8080

4️⃣ Verify

Visit:

http://localhost:8080/api/health


Expected response:

{"status": "ok"}

💻 Frontend Setup (React)
1️⃣ Open a new terminal
cd frontend
npm install

2️⃣ Start the React app
npm run dev


✅ The frontend runs at:

http://localhost:3000

3️⃣ Proxy Configuration

vite.config.js automatically proxies /api requests to the Flask backend.

🧪 Running Tests

To run backend automated tests:

cd backend
pytest -q


✅ Example output:

1 passed in 0.45s

API Endpoints

| Method     | Endpoint                        | Description                   |
| ---------- | ------------------------------- | ----------------------------- |
| **POST**   | `/api/tasks`                    | Create a new task             |
| **GET**    | `/api/tasks`                    | List all tasks                |
| **GET**    | `/api/tasks/<id>`               | Retrieve a single task        |
| **PUT**    | `/api/tasks/<id>`               | Update a task                 |
| **DELETE** | `/api/tasks/<id>`               | Delete a task                 |
| **POST**   | `/api/tasks/<task_id>/comments` | Create a comment under a task |
| **GET**    | `/api/tasks/<task_id>/comments` | Get all comments for a task   |
| **PUT**    | `/api/comments/<id>`            | Update a comment              |
| **DELETE** | `/api/comments/<id>`            | Delete a comment              |

Pull Request Guidelines

Each task or feature must be implemented in a separate branch and submitted via a Pull Request (PR) to maintain clean version control.

🔹 Backend PR

Branch: feat/comments-backend

Title: feat: add comments CRUD API with automated tests

Includes: Flask API for comments, model updates, test cases

🔹 Frontend PR

Branch: feat/tasks-frontend

Title: feat: add tasks management UI with inline comments panel

Includes: React page for task list, add/delete functionality, inline comment display

✅ PR Checklist

 Code self-reviewed

 All endpoints manually tested

 Pytest executed successfully

 README updated

 Debug prints removed

 No unused imports

👥 Contributors
Name	Role	GitHub
Amol Arora	Fullstack Developer	@Amolarora-75
🏁 Final Notes

Always test locally before pushing commits.

Keep commits small, descriptive, and atomic.

Create separate branches for each task or feature.

Ensure both backend and frontend servers run without conflicts.

Use PRs for all submissions to maintain clean collaboration and review workflow.
