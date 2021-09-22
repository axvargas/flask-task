'''
Created Date: Tuesday September 14th 2021 11:12:59 pm
Author: Andrés X. Vargas
-----
Last Modified: Wednesday September 22nd 2021 12:51:28 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
import unittest

from flask.helpers import flash, url_for

from app import create_app
from flask import request, make_response, redirect, render_template, session
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from app.firestore_service import delete_todo, get_todos, create_todo, delete_todo, update_todo
from flask_login import login_required, current_user
app = create_app()

todos = ['TODO1', 'TODO2', 'TODO3']


@app.cli.command()
def test():
    print('testing...')
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.errorhandler(404)
def not_found(error):
    context = {'error': error, 'error_code': 404}
    return render_template('error.html', **context)


@app.errorhandler(500)
def not_found(error):
    context = {'error': error, 'error_code': 500}
    return render_template('error.html', **context)


@app.errorhandler(405)
def not_found(error):
    context = {'error': error, 'error_code': 405}
    return render_template('error.html', **context)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello_world():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()
    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form
    }

    if todo_form.validate_on_submit():
        todo_data = {
            'description': todo_form.description.data,
            'done': False
        }
        create_todo(user_id=username, todo_data=todo_data)
        flash('Todo created successfully!', 'success')
        return redirect('/hello')

    return render_template('hello.html', **context)


@app.route('/todo/delete/<todo_id>', methods=['POST'])
@login_required
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('hello_world'))


@app.route('/todo/update/<todo_id>/<int:done>', methods=['POST'])
@login_required
def update(todo_id, done):
    user_id = current_user.id
    todo_data = {
        'done': not done
    }
    update_todo(user_id=user_id, todo_id=todo_id, todo_data=todo_data)
    flash('Todo updated successfully!', 'success')
    return redirect(url_for('hello_world'))
