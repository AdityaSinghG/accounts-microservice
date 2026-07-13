"""
Accounts Microservice Initialization
"""

import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database object
db = SQLAlchemy()


def create_app():
    """
    Application Factory
    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URI", "sqlite:///accounts.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "this_is_a_secret_key"
    )

    # Initialize database
    db.init_app(app)

    # Configure Logging
    logging.basicConfig(level=logging.INFO)

    with app.app_context():
        from service import models
        db.create_all()

    from service.routes import api

    app.register_blueprint(api)

    return app
