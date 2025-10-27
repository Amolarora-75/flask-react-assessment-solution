from flask import Blueprint, request, jsonify
from database import db
from models import Task, Comment

api = Blueprint('api', __name__)

# ---------------- Tasks ----------------
@api.post('/api/tasks')
def create_task():
    data = request.get_json() or {}
    title = (data.get('title') or '').strip()
    description = (data.get('description') or '').strip()
    if not title:
        return jsonify({'error': 'title is required'}), 400
    t = Task(title=title, description=description)
    db.session.add(t)
    db.session.commit()
    return jsonify({'id': t.id, 'title': t.title, 'description': t.description}), 201

@api.get('/api/tasks')
def list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([{'id': t.id, 'title': t.title, 'description': t.description} for t in tasks]), 200

@api.get('/api/tasks/<int:task_id>')
def get_task(task_id):
    t = Task.query.get(task_id)
    if not t:
        return jsonify({'error':'Task not found'}), 404
    return jsonify({'id': t.id, 'title': t.title, 'description': t.description}), 200

@api.put('/api/tasks/<int:task_id>')
def update_task(task_id):
    t = Task.query.get(task_id)
    if not t:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json() or {}
    if 'title' in data:
        title = (data.get('title') or '').strip()
        if not title:
            return jsonify({'error': 'title cannot be empty'}), 400
        t.title = title
    if 'description' in data:
        t.description = (data.get('description') or '').strip()
    db.session.commit()
    return jsonify({'id': t.id, 'title': t.title, 'description': t.description}), 200

@api.delete('/api/tasks/<int:task_id>')
def delete_task(task_id):
    t = Task.query.get(task_id)
    if not t:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(t)
    db.session.commit()
    return '', 204

# ------------- Comments ----------------
@api.get('/api/tasks/<int:task_id>/comments')
def list_comments(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc()).all()
    return jsonify([{
        'id': c.id, 'task_id': c.task_id, 'body': c.body, 'author': c.author,
        'created_at': c.created_at.isoformat(), 'updated_at': c.updated_at.isoformat() if c.updated_at else None
    } for c in comments]), 200

@api.post('/api/tasks/<int:task_id>/comments')
def create_comment(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json() or {}
    body = (data.get('body') or '').strip()
    author = (data.get('author') or None)
    if not body:
        return jsonify({'error': 'body is required'}), 400
    c = Comment(task_id=task_id, body=body, author=author)
    db.session.add(c)
    db.session.commit()
    return jsonify({'id': c.id, 'task_id': c.task_id, 'body': c.body, 'author': c.author}), 201

@api.put('/api/comments/<int:comment_id>')
def update_comment(comment_id):
    c = Comment.query.get(comment_id)
    if not c:
        return jsonify({'error': 'Comment not found'}), 404
    data = request.get_json() or {}
    if 'body' in data:
        body = (data.get('body') or '').strip()
        if not body:
            return jsonify({'error': 'body cannot be empty'}), 400
        c.body = body
    if 'author' in data:
        c.author = (data.get('author') or None)
    db.session.commit()
    return jsonify({'id': c.id, 'task_id': c.task_id, 'body': c.body, 'author': c.author}), 200

@api.delete('/api/comments/<int:comment_id>')
def delete_comment(comment_id):
    c = Comment.query.get(comment_id)
    if not c:
        return jsonify({'error': 'Comment not found'}), 404
    db.session.delete(c)
    db.session.commit()
    return '', 204
