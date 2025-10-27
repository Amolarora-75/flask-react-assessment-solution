# Fullstack Assessment — Flask + React

This project delivers:
- **Backend (Flask + SQLite)**: CRUD for **Tasks** and **Comments** (comments belong to a task).
- **Tests (pytest)**: Coverage for comment CRUD flow.
- **Frontend (Vite + React)**: Simple Tasks UI with create/delete and add/delete comments per task.

## 1) Run Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Backend runs at **http://localhost:8080**.

### API Quickstart
- Create Task: `POST /api/tasks`  body: `{ "title":"T1", "description":"..." }`
- List Tasks: `GET /api/tasks`
- Create Comment: `POST /api/tasks/{taskId}/comments` body: `{ "body":"Hi", "author":"Amol" }`
- List Comments: `GET /api/tasks/{taskId}/comments`
- Update Comment: `PUT /api/comments/{commentId}`
- Delete Comment: `DELETE /api/comments/{commentId}`

## 2) Run Frontend
```bash
cd frontend
npm install
npm run dev
```
Open **http://localhost:3000** (proxy to backend on `/api`).

## 3) Run Tests
```bash
cd backend
pytest -q
```

## 4) What to record in your video
- Brief overview of the endpoints.
- Show Postman/Thunder Client hitting the endpoints (create task → add comment → update → delete).
- Show the React page: add a task, then add/delete comments.

## 5) Notes
- This project uses **SQLite** for simplicity. It runs out-of-the-box (no external DB required).
- CORS is enabled for the frontend to call the backend.
```
