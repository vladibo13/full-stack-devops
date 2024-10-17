from flask import Flask
from .extensions import db
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()  # Create tables

    return app