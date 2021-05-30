from django.test import TestCase
from .forms import LoginForm
from principal.models import User
import datetime

class LoginFormTestCase(TestCase):




    #Formato válido y usuario existente en la aplicación
    def test_create_login_form(self):

        u = User(username='user1')
        u.set_password('hola1234')
        u.save()

        form_data = {'username': 'user1', 'password': 'hola1234'}
        form = LoginForm(data=form_data)

        self.assertTrue(form.is_valid())

    #Credenciales incorrectos
    def test_create_login_form_incorrect(self):

        u = User(username='user1')
        u.set_password('hola1234')
        u.save()

        form_data = {'username': 'user2', 'password': 'hola1234'}
        form = LoginForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Username vacío
    def test_create_login_form_incorrect_username_blank(self):

        u = User(username='user1')
        u.set_password('hola1234')
        u.save()

        form_data = {'username': '', 'password': 'hola1234'}
        form = LoginForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Password vacío
    def test_create_login_form_incorrect_username_blank(self):

        u = User(username='user1')
        u.set_password('hola1234')
        u.save()

        form_data = {'username': 'user1', 'password': ''}
        form = LoginForm(data=form_data)

        self.assertFalse(form.is_valid())