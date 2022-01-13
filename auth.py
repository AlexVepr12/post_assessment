from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user

from .models import Accesor, Users

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    check_user = Users.query.filter(Users.email.like(email)).first()
    if check_user:
        user = Accesor.query.filter(Accesor.id == check_user.id).first()
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))

    if not check_user:
        flash('Неверный логин или пароль!')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page


@auth.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')
