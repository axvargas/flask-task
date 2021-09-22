'''
Created Date: Thursday September 16th 2021 8:25:55 pm
Author: Andrés X. Vargas
-----
Last Modified: Friday September 17th 2021 12:38:13 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from flask.helpers import url_for
from flask_testing import TestCase
from flask import current_app
from werkzeug.wrappers import response
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects_to_hello_world(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello_world'))
    
    def test_hello_world_success(self):
        response = self.client.get(url_for('hello_world'))
        self.assert200(response)

    def test_hello_world_post(self):
        response = self.client.post(url_for('hello_world'))
        self.assert200(response)

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', current_app.blueprints)
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)
    
    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')
    
    def test_auth_login_post(self):
        fake_form = {
            'username': 'admin',
            'password': 'admin'
        }

        response = self.client.post(url_for('auth.login'), data=fake_form)

        self.assertRedirects(response, url_for('index'))