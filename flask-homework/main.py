from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    app.logger.info(print('Hello func was called'))
    return 'Hello World!'


app.run()
