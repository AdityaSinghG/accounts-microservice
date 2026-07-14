"""
Accounts Microservice
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
app.config.from_object("config.Config")

# Initialize extensions
db = SQLAlchemy(app)

# Security headers with Talisman
talisman = Talisman(app, force_https=False)

# CORS policy
CORS(app)

from service import routes  # noqa: E402, F401
