from app_data import app
from flask import request, redirect


@app.route('/')
def home():
    return 'You are on RobotApp home page'


@app.route('/hello')
def hello():
    app.logger.info(f'Hello func was called')
    return 'Hello World!'


@app.route('/users')
def users():
    return (
        '<ul>'
        '<li>Roman</li>'
        '<li>Anton</li>'
        '<li>Nazar</li>'
        '<li>Dima</li>'
        '<li>Andrii</li>'
        '</ul>'
    )


@app.route('/users/<user_id>')
def users_id_check(user_id):
    if user_id.isdigit():
        if int(user_id) % 2 == 0:
            return f'Requested user ID: {user_id}'
        else:
            return '', 404
    else:
        return 'Users ID have to be digit', 404


@app.route('/books')
def books():
    return ('<ul>'
    "<li>Harry Potter and the Philosopher's Stone</li>"
    '<li>Harry Potter and the Chamber of Secrets</li>'
    '<li>Harry Potter and the Prisoner of Azkaban</li>'
    '<li>Harry Potter and the Goblet of Fire</li>'
    '<li>Harry Potter and the Order of the Phoenix</li>'
    '<li>Harry Potter and the Half-Blood Prince</li>'
    '<li>Harry Potter and the Deathly Hallows</li>'
    '</ul>')


@app.route('/books/<books_title>')
def books_title_check(books_title):
    return f'Requested book: {books_title.capitalize()}'


@app.route('/params')
def params_page():
    _args = (
            '<style>table, th, td {border: 1px solid black;border-collapse: collapse;}'
            '</style><table><tr><th>Parameter</th><th>Value</th></tr>'
    )
    for key, value in request.args.items():
        _args += f'<tr><th>{key}</th><th>{value}</th></tr>'
    _args += '</table>'
    print(_args)
    return f'{_args}'


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        html_form = (
            "<form method=POST action='/login'>"
            "<input type='string' name='username' value=''/>"
            "<input type='password' name='password' value=''/>"
            "<button type='submit'>Login</button>"
            "</form>"
        )
        return html_form
    elif request.method == 'POST':
        if 'password' and 'username' in request.form:
            return redirect('/users')
        else:
            return 'Password incorrect', 404
