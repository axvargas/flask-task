'''
Created Date: Thursday September 16th 2021 10:19:28 pm
Author: Andrés X. Vargas
-----
Last Modified: Tuesday September 21st 2021 10:50:00 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from flask_login.utils import login_required
from . import auth
from app.forms import LoginForm, SignUpForm
from flask import render_template, redirect, url_for, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.firestore_service import get_user, create_user
from app.models import UserData, UserModel

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    sign_up_form = SignUpForm()
    context = {
        'sign_up_form': sign_up_form
    }
    if sign_up_form.validate_on_submit():
        username = sign_up_form.username.data
        password = sign_up_form.password.data
        user_doc = get_user(username)
        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            create_user(user_data)
            flash('Usuario creado exitosamente')
            user_model = UserModel(user_data)
            login_user(user_model)
            flash('Bienvenido')
            return redirect(url_for('hello_world'))
        else:
            flash('El usuario ya existe')
            return redirect(url_for('auth.sign_up'))
    return render_template('sign_up.html', **context)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user_doc = get_user(username)
        if user_doc.to_dict() is not None:
            if check_password_hash(user_doc.to_dict()['password'], password):
                user_data = UserData(
                    username=username,
                    password=password,
                )
                user = UserModel(user_data)
                login_user(user)
                flash('Bienvenido {}'.format(username), 'success')
                return redirect(url_for('hello_world'))
            else:
                flash('Credenciales incorrectas', 'error')
        else:
            flash('Usuario o contraseña incorrectos', 'warning')
        
        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada', 'info')
    session.pop('username', None)

    return redirect(url_for('auth.login'))