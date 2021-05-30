from django.test import TestCase
from .forms import CreateTrainingForm
from principal.models import User
import datetime

class CreateTraningFormTestCase(TestCase):
    
    def test_create_training(self):

        form_data = {'name': 'Training Test', 'description': 'Description Test',
                    'inputPatients': 'Test Patient', 'inputActivities': 'Test Activity'}
        form = CreateTrainingForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_create_training_no_name(self):

        form_data = {'name': '', 'description': 'Description Test',
                    'inputPatients': 'Test Patient', 'inputActivities': 'Test Activity'}
        form = CreateTrainingForm(data=form_data)

        self.assertFalse(form.is_valid())
    
    def test_create_training_no_patients(self):

        form_data = {'name': 'Training Test', 'description': 'Description Test',
                    'inputPatients': '', 'inputActivities': 'Test Activity'}
        form = CreateTrainingForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_create_training_no_activities(self):

        form_data = {'name': 'Training Test', 'description': 'Description Test',
                    'inputPatients': 'Test Patient', 'inputActivities': ''}
        form = CreateTrainingForm(data=form_data)

        self.assertFalse(form.is_valid())