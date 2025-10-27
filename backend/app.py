import os
from flask import Flask, jsonify
from flask_cors import CORS
from database import db
from routes import api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(api)
    @app.get('/api/health')
    def health():
        return jsonify({'status': 'ok'}), 200
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
