from app_data import app
from flask import request, redirect, render_template, session
import  random


app.secret_key = b'robot'


@app.route('/')
def home():
    return 'You are on RobotApp home page'


@app.route('/hello')
def hello():
    app.logger.info(f'Hello func was called')
    return 'Hello World!'


@app.route('/users')
def users():
    current_user = session.get('user')
    if current_user:
        users_list = ['Voldemort',
                      'Sirius Black',
                      'Remus Lupin',
                      'Neville Longbottom',
                      'Minerva McGonagall',
                      'Albus Dumbledore',
                      'Severus Snape']
        requested_list = []
        random_list = random.sample(users_list, random.randint(1, len(users_list)))
        for user in random_list:
            requested_list += (user,)
        return render_template('list.html', name='Users', list=requested_list, username=current_user)
    else:
        return redirect('/login')


@app.route('/users/<int:user_id>')
def users_id_check(user_id):
    current_user = session.get('user')
    if current_user:
        if int(user_id) % 2 == 0:
            return render_template('user_id.html', name=f'User: {user_id}', user_id=user_id, username=current_user)
        else:
            return '', 404
    else:
        return redirect('/login')


@app.route('/books')
def books():
    current_user = session.get('user')
    if current_user:
        books_list = [
            "Harry Potter and the Philosopher's Stone",
            'Harry Potter and the Chamber of Secrets',
            'Harry Potter and the Prisoner of Azkaban',
            'Harry Potter and the Goblet of Fire',
            'Harry Potter and the Order of the Phoenix',
            'Harry Potter and the Half-Blood Prince',
            'Harry Potter and the Deathly Hallows'
        ]
        requested_list = []
        random_list = random.sample(books_list, random.randint(1, len(books_list)))
        for book in random_list:
            requested_list += (book,)
        return render_template('list.html', name='Books', list=requested_list, username=current_user)
    else:
        return redirect('/login')


@app.route('/books/<books_title>')
def books_title_check(books_title):
    current_user = session.get('user')
    if current_user:
        return render_template('new_book.html', name=f'{books_title}', book_name=books_title, username=current_user)
    else:
        return redirect('/login')


@app.route('/params')
def params_page():
    current_user = session.get('user')
    if current_user:
        return render_template('params.html', list=request.args.items(), username=current_user)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if 'password' and 'username' in request.form:
            username = request.form.get('username')
            session['user'] = username
            return redirect('/users')
    else:
        return 'Password incorrect', 404
