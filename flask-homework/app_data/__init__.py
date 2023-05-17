from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from .config import AppConfig


db = SQLAlchemy()
app = Flask(__name__)

dictConfig({
    "version": 1,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"}
    },
    "root": {"handlers": ["console"], "level": "INFO"},
})

app.config.from_object(AppConfig)
db.init_app(app)

from .views import *
from .models import *

with app.app_context():
    db.create_all()

