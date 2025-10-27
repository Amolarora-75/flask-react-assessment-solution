import pytest
from app import create_app
from database import db

@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app.test_client()

def test_comment_crud_flow(client):
    # Create a task
    resp = client.post('/api/tasks', json={"title":"Task A","description":"desc"})
    assert resp.status_code == 201
    task_id = resp.get_json()["id"]

    # List comments (empty)
    res = client.get(f'/api/tasks/{task_id}/comments')
    assert res.status_code == 200
    assert res.get_json() == []

    # Create comment
    res = client.post(f'/api/tasks/{task_id}/comments', json={"body":"First!","author":"Amol"})
    assert res.status_code == 201
    comment = res.get_json()
    cid = comment["id"]

    # Update comment
    res = client.put(f'/api/comments/{cid}', json={"body":"Edited"})
    assert res.status_code == 200
    assert res.get_json()["body"] == "Edited"

    # Delete comment
    res = client.delete(f'/api/comments/{cid}')
    assert res.status_code == 204

    # Confirm deletion by listing
    res = client.get(f'/api/tasks/{task_id}/comments')
    assert res.status_code == 200
    assert res.get_json() == []
