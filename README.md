# 🧠 Flask + React Fullstack Assessment  
> A complete end-to-end task management and commenting system built using **Flask (Python)** and **React (Vite)** — with RESTful APIs, database integration, automated tests, and a simple frontend UI.

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Backend Setup (Flask)](#backend-setup-flask)
5. [Frontend Setup (React)](#frontend-setup-react)
6. [Running Tests](#running-tests)
7. [API Endpoints](#api-endpoints)
8. [Creating Pull Requests](#creating-pull-requests)
9. [Video Demonstration](#video-demonstration)
10. [Contributors](#contributors)

---

## 🧩 Overview
This project was developed as part of a **Fullstack Engineer Assessment**. It implements:
- **Backend (Flask + SQLite)** for RESTful Task and Comment management APIs  
- **Frontend (React + Vite)** to create, view, and delete tasks and comments  
- **Automated Testing** using Pytest for backend validation  

### ✨ Features
- Task CRUD (Create, Read, Update, Delete)  
- Comment CRUD (linked to each Task)  
- RESTful API design with validation  
- Full test coverage for comment endpoints  
- React-based frontend with real-time UI updates  
- Proxy configuration to connect React → Flask easily  

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


