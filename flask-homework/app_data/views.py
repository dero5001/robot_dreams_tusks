from dotenv import load_dotenv
from app_data import app
from flask import request, redirect, render_template, session
from .models import User, Book, Purchase
import random
import os

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')


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
        users_list = User.query.all()
        return render_template('list.html', name='Users', list=users_list, username=current_user)
    else:
        return redirect('/login')


@app.route('/users/<int:user_id>')
def users_id_check(user_id):
    current_user = session.get('user')
    if current_user:
        users_list = User.query.all()
        for user in users_list:
            if user.id == user_id:
                return render_template('user_id.html', user_id=user.id, name=user.name, username=current_user)
        else:
            return '', 404
    else:
        return redirect('/login')


@app.route('/books')
def books():
    current_user = session.get('user')
    if current_user:
        books_list = Book.query.all()
        return render_template('list.html', name='Books', list=books_list, username=current_user)
    else:
        return redirect('/login')


@app.route('/books/<int:book_id>')
def books_title_check(book_id):
    current_user = session.get('user')
    if current_user:
        books_list = Book.query.all()
        for book in books_list:
            if book.id == book_id:
                return render_template('book_id.html', book_id=book.id, name=book.name, username=current_user)
        else:
            return '', 404
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


@app.route('/purchases')
def get_purchases():
    current_user = session.get('user')
    if current_user:
        purchases_list = Purchase.query.all()
        return render_template('p_list.html', name='purchases', list=purchases_list, username=current_user)
    else:
        return redirect('/login')


@app.route('/purchases/<int:purchase_id>')
def current_purchase(purchase_id):
    current_user = session.get('user')
    if current_user:
        purchases_list = Purchase.query.all()
        for purchase in purchases_list:
            if purchase.id == purchase_id:
                return render_template('purchase_id.html', purchase=purchase, username=current_user)
        else:
            return '', 404
    else:
        return redirect('/login')
