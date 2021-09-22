'''
Created Date: Thursday September 16th 2021 9:12:30 pm
Author: Andrés X. Vargas
-----
Last Modified: Tuesday September 21st 2021 9:14:33 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_manager
from .config import Config
from .auth import auth
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():    
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    login_manager.init_app(app)
    app.register_blueprint(auth)
    
    return app