from django.test import TestCase
from .forms import CreateDoctorForm, CreatePatientForm, UpdateDoctorForm, UpdatePasswordForm, UpdatePatientForm
from principal.models import User
import datetime



class CreateDoctorFormCase(TestCase):

    #Formato válido campos doctor
    def test_create_doctor_form(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertTrue(form.is_valid())


    #Username doctor ya existente en la aplicación
    def test_create_doctor_exists(self):

        u = User(username='user1')
        u.set_password('hola1234')
        u.save()

        form_data = {'username': 'user1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Email doctor ya existente en la aplicación
    def test_create_doctor_email_exists(self):

        u = User(username='user1', email='test1@gmail.com')
        u.set_password('123')
        u.save()

        form_data = {'username': 'user2', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Fecha de nacimiento posterior a la actual
    def test_create_doctor_incorrect_birth_date(self):

        today = datetime.date.today()

        day = datetime.timedelta(days=1)

        date = datetime.datetime.strftime(today + day, '%Y-%m-%d')

        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': date, 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Password con menos de 6 caracteres
    def test_create_doctor_incorrect_password(self):

        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': '123',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())
    
    #Username vacío
    def test_create_doctor_incorrect_username_blank(self):
        form_data = {'username': '', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    
    #Password vacío
    def test_create_doctor_incorrect_password_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': '',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #First_name vacío
    def test_create_doctor_incorrect_first_name_blank(self):
        form_data = {'username': 'test1', 'first_name': '', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Last_name vacío
    def test_create_doctor_incorrect_last_name_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': '', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Specialty vacío
    def test_create_doctor_incorrect_specialty_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': '', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())
    
    #Birth_date vacío
    def test_create_doctor_incorrect_birth_date_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #email vacío
    def test_create_doctor_incorrect_email_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'', 'password': 'hola1234',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = CreateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

class CreatePatientFormCase(TestCase):

    #Formato válido campos patient
    def test_create_patient_form(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertTrue(form.is_valid())


    #Username patient ya existente en la aplicación
    def test_create_patient_exists(self):

        u = User(username='user1')
        u.set_password('123')
        u.save()

        form_data = {'username': 'user1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Email patient ya existente en la aplicación
    def test_create_patient_email_exists(self):

        u = User(username='user1', email='test1@gmail.com')
        u.set_password('123')
        u.save()

        form_data = {'username': 'user2', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Fecha de nacimiento posterior a la actual
    def test_create_patient_incorrect_birth_date(self):

        today = datetime.date.today()

        day = datetime.timedelta(days=1)

        date = datetime.datetime.strftime(today + day, '%Y-%m-%d')

        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': date, 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Password con menos de 6 caracteres
    def test_create_patient_incorrect_password(self):

        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': '123',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())
    
    #Username vacío
    def test_create_patient_incorrect_username_blank(self):
        form_data = {'username': '', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    
    #Password vacío
    def test_create_patient_incorrect_password_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': '',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #First_name vacío
    def test_create_patient_incorrect_first_name_blank(self):
        form_data = {'username': 'test1', 'first_name': '', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Last_name vacío
    def test_create_patient_incorrect_last_name_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': '', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Sickness vacío
    def test_create_patient_incorrect_specialty_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': '', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())
    
    #Birth_date vacío
    def test_create_patient_incorrect_birth_date_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #email vacío
    def test_create_patient_incorrect_email_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #address vacío
    def test_create_patient_incorrect_address_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "", 'comments': 'Test comments', 'city': 'Test city', 'address': '', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #city vacío
    def test_create_patient_incorrect_city_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': '', 'address': 'Test address', 'doctor': 'doctor test'}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #doctor vacío
    def test_create_patient_incorrect_doctor_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': ''}
        form = CreatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())


class UpdatePatientTest(TestCase):
       #Formato válido campos patient
    def test_update_patient_form(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertTrue(form.is_valid())

    #Fecha de nacimiento posterior a la actual
    def test_update_patient_incorrect_birth_date(self):

        today = datetime.date.today()

        day = datetime.timedelta(days=1)

        date = datetime.datetime.strftime(today + day, '%Y-%m-%d')

        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'sickness': 'sickness test', 'birth_date': date, 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    
    #Username vacío
    def test_update_patient_incorrect_username_blank(self):
        form_data = {'username': '', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())



    #First_name vacío
    def test_update_patient_incorrect_first_name_blank(self):
        form_data = {'username': 'test1', 'first_name': '', 'last_name': 'Test1', 'email':'test1@gmail.com', 'password': 'hola1234',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Last_name vacío
    def test_update_patient_incorrect_last_name_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': '', 'email':'test1@gmail.com',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Sickness vacío
    def test_update_patient_incorrect_specialty_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com',
                    'sickness': '', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())
    
    #Birth_date vacío
    def test_update_patient_incorrect_birth_date_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'sickness': 'sickness test', 'birth_date': "", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #email vacío
    def test_update_patient_incorrect_email_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'', 
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #address vacío
    def test_update_patient_incorrect_address_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'sickness': 'sickness test', 'birth_date': "", 'comments': 'Test comments', 'city': 'Test city', 'address': '', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #city vacío
    def test_update_patient_incorrect_city_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'', 
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': '', 'address': 'Test address', 'doctor': 'doctor test'}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

    #doctor vacío
    def test_update_patient_incorrect_doctor_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com',
                    'sickness': 'sickness test', 'birth_date': "1999-05-19", 'comments': 'Test comments', 'city': 'Test city', 'address': 'Test address', 'doctor': ''}
        form = UpdatePatientForm(data=form_data)

        self.assertFalse(form.is_valid())

class UpdateDoctorFormCase(TestCase):

    #Formato válido campos doctor
    def test_update_doctor_form(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertTrue(form.is_valid())

    #Fecha de nacimiento posterior a la actual
    def test_update_doctor_incorrect_birth_date(self):

        today = datetime.date.today()

        day = datetime.timedelta(days=1)

        date = datetime.datetime.strftime(today + day, '%Y-%m-%d')

        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'specialty': 'specialty test', 'birth_date': date, 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Username vacío
    def test_update_doctor_incorrect_username_blank(self):
        form_data = {'username': '', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #First_name vacío
    def test_update_doctor_incorrect_first_name_blank(self):
        form_data = {'username': 'test1', 'first_name': '', 'last_name': 'Test1', 'email':'test1@gmail.com',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Last_name vacío
    def test_update_doctor_incorrect_last_name_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': '', 'email':'test1@gmail.com',
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Specialty vacío
    def test_update_doctor_incorrect_specialty_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'specialty': '', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())
    
    #Birth_date vacío
    def test_update_doctor_incorrect_birth_date_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'test1@gmail.com', 
                    'specialty': 'specialty test', 'birth_date': "", 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

    #email vacío
    def test_update_doctor_incorrect_email_blank(self):
        form_data = {'username': 'test1', 'first_name': 'Test1', 'last_name': 'Test1', 'email':'', 
                    'specialty': 'specialty test', 'birth_date': "1999-05-19", 'comments': 'Test comments'}
        form = UpdateDoctorForm(data=form_data)

        self.assertFalse(form.is_valid())

class UpdatePasswordTest(TestCase):

    #Formato válido contraseñas
    def test_update_password_correct(self):
        form_data = {'password1': 'test12', 'password2': 'test12'}
        form = UpdatePasswordForm(data=form_data)

        self.assertTrue(form.is_valid())

    #Formato inválido contraseñas
    def test_update_password_invalid_format(self):
        form_data = {'password1': 'test1', 'password2': 'test1'}
        form = UpdatePasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Contraseña 1 vacia
    def test_update_password1_blank(self):
        form_data = {'password1': '', 'password2': 'test12'}
        form = UpdatePasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    #Contraseña 2 vacia
    def test_update_password2_blank(self):
        form_data = {'password1': 'test12', 'password2': ''}
        form = UpdatePasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

        #Contraseña 2 vacia
    def test_update_different_password(self):
        form_data = {'password1': 'test12', 'password2': 'test13'}
        form = UpdatePasswordForm(data=form_data)

        self.assertFalse(form.is_valid())