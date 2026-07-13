"""
Accounts Microservice
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask application
app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = "dev_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URI",
    "sqlite:///accounts.db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database object
db = SQLAlchemy(app)

# Import routes after app/db initialization
from service import routes
