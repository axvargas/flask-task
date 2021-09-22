'''
Created Date: Thursday September 16th 2021 9:51:20 pm
Author: Andrés X. Vargas
-----
Last Modified: Wednesday September 22nd 2021 12:40:03 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sing up')

class TodoForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Update')
