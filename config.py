"""
Application Configuration
"""

import os


class Config:
    """Configuration"""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "sqlite:///accounts.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
