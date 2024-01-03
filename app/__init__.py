from flask import Flask
from app.model import db, user
from config import Config
from app.controller import api as api_blueprint
from flask_cors import CORS

def create_app(config_class=Config):
    app = Flask(__name__)
    # Enable CORS for all routes
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)

    # Create the database tables
    with app.app_context():
        db.create_all()

    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
