# Imports from Flask
from flask import Flask, render_template, request
# Extension for implementing SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy
import os
# Take environment variables from .env
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initializing extensions
    db.init_app(app)

    # Imports from subpackages (views)
    with app.app_context():
        from app.main.views import main
        app.register_blueprint(main)

    from app.main.views import page_not_found
    app.register_error_handler(404, page_not_found)

    return app
