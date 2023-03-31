from logging.config import dictConfig
from flask import Flask

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

app = Flask(__name__)

@app.route('/hello')
def hello():
    app.logger.info(f'Hello func was called')
    return 'Hello World!'


app.run()
