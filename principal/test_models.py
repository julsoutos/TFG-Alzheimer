from django.test import TestCase
from principal.models import User, Doctor, Patient, Activity, Solution, Training, Activity_Result, Patient_training, Activity_Training

class UserModelTest(TestCase):

    def setUp(self):
        self.test_user =  User(is_medic = False, is_patient = True, first_name = 'User Test', last_name = 'Model Test 1', comments = 'This is a test', save_session = False)
        self.test_user.save()

    def test_user_creation(self):
       user_test = self.test_user

       self.assertEquals(user_test.is_medic, False)
       self.assertEquals(user_test.is_patient, True)
       self.assertEquals(user_test.first_name, 'User Test')
       self.assertEquals(user_test.last_name, 'Model Test 1')
       self.assertEquals(user_test.comments, 'This is a test')
       self.assertEquals(user_test.save_session, False)

    def tearDown(self):
        self.test_user.delete()

class DoctorModelTest(TestCase):

    def setUp(self):
        self.test_user =  User(is_medic = True, is_patient = False, first_name = 'User Test', last_name = 'Model Test 1', comments = 'This is a test', save_session = False)
        self.test_user.save()
        self.test_doctor = Doctor(user = self.test_user, specialty = 'Cirujano')
        self.test_doctor.save()

    def test_doctor_creation(self):
       doctor_test = self.test_doctor

       self.assertEquals(doctor_test.user.is_medic, True)
       self.assertEquals(doctor_test.user.is_patient, False)
       self.assertEquals(doctor_test.user.first_name, 'User Test')
       self.assertEquals(doctor_test.user.last_name, 'Model Test 1')
       self.assertEquals(doctor_test.user.comments, 'This is a test')
       self.assertEquals(doctor_test.user.save_session, False)
       self.assertEquals(doctor_test.specialty, 'Cirujano')

    def tearDown(self):
        self.test_doctor.delete()
        self.test_user.delete()

class PatientModelTest(TestCase):

    def setUp(self):
        self.test_user1 =  User(is_medic = True, is_patient = False, username="username1", first_name = 'User Test', last_name = 'Model Test 1', comments = 'This is a test', save_session = False)
        self.test_user1.save()
        self.test_user2 =  User(is_medic = False, is_patient = True, username="username2", first_name = 'User Test', last_name = 'Model Test 2', comments = 'This is a test', save_session = False)
        self.test_user2.save()
        self.test_doctor = Doctor(user = self.test_user1, specialty = 'Cirujano')
        self.test_doctor.save()
        self.test_patient = Patient(doctor = self.test_doctor, user = self.test_user2, sickness = 'Alzheimer')    
        self.test_patient.save()

    def test_patient_creation(self):
       patient_test = self.test_patient

       self.assertEquals(patient_test.user.is_medic, False)
       self.assertEquals(patient_test.user.is_patient, True)
       self.assertEquals(patient_test.user.first_name, 'User Test')
       self.assertEquals(patient_test.user.last_name, 'Model Test 2')
       self.assertEquals(patient_test.user.comments, 'This is a test')
       self.assertEquals(patient_test.user.save_session, False)
       self.assertEquals(patient_test.sickness, 'Alzheimer')

    def tearDown(self):
        self.test_patient.delete()
        self.test_doctor.delete()
        self.test_user1.delete()
        self.test_user2.delete()

class ActivityModelTest(TestCase):

    def setUp(self):
        self.test_activity =  Activity(name = 'Test Activity 1', title = 'Title Test Activity', description = 'This is a test')
        self.test_activity.save()

    def test_activity_creation(self):
       activity_test = self.test_activity

       self.assertEquals(activity_test.name, 'Test Activity 1')
       self.assertEquals(activity_test.title, 'Title Test Activity')
       self.assertEquals(activity_test.description, 'This is a test')

    def tearDown(self):
        self.test_activity.delete()

class SolutionModelTest(TestCase):

    def setUp(self):
        self.test_activity =  Activity(name = 'Test Activity 1', title = 'Title Test Activity', description = 'This is a test')
        self.test_activity.save()
        self.test_solution = Solution(activity = self.test_activity, name = 'Test Solution 1', solution = 'Solution Test 1')
        self.test_solution.save()

    def test_solution_creation(self):
       solution_test = self.test_solution

       self.assertEquals(solution_test.activity.name, 'Test Activity 1')
       self.assertEquals(solution_test.activity.title, 'Title Test Activity')
       self.assertEquals(solution_test.activity.description, 'This is a test')
       self.assertEquals(solution_test.name, 'Test Solution 1')
       self.assertEquals(solution_test.solution, 'Solution Test 1')

    def tearDown(self):
        self.test_solution.delete()
        self.test_activity.delete()

class TrainingModelTest(TestCase):

    def setUp(self):
        self.test_user =  User(is_medic = True, is_patient = False, username="username1", first_name = 'User Test', last_name = 'Model Test 1', comments = 'This is a test', save_session = False)
        self.test_user.save()
        self.test_doctor = Doctor(user = self.test_user, specialty = 'Cirujano')
        self.test_doctor.save()
        self.test_training = Training(name = 'Training Test 1', description = 'This is a test', doctor = self.test_doctor)
        self.test_training.save()

    def test_training_creation(self):
       training_test = self.test_training

       self.assertEquals(training_test.name, 'Training Test 1')
       self.assertEquals(training_test.description, 'This is a test')
       self.assertEquals(training_test.doctor.user.first_name, 'User Test')

    def tearDown(self):
        self.test_training.delete()
        self.test_doctor.delete()
        self.test_user.delete()


class ActivityResultModelTest(TestCase):

    def setUp(self):
        self.test_user1 =  User(is_medic = True, is_patient = False, username="username1", first_name = 'User Test', last_name = 'Model Test 1', comments = 'This is a test', save_session = False)
        self.test_user1.save()
        self.test_user2 =  User(is_medic = False, is_patient = True, username="username2", first_name = 'User Test', last_name = 'Model Test 2', comments = 'This is a test', save_session = False)
        self.test_user2.save()
        self.test_doctor = Doctor(user = self.test_user1, specialty = 'Cirujano')
        self.test_doctor.save()
        self.test_patient = Patient(doctor = self.test_doctor, user = self.test_user2, sickness = 'Alzheimer')    
        self.test_patient.save()
        self.test_activity =  Activity(name = 'Test Activity 1', title = 'Title Test Activity', description = 'This is a test')
        self.test_activity.save()
        self.test_solution = Solution(activity = self.test_activity, name = 'Test Solution 1', solution = 'Solution Test 1')
        self.test_solution.save()
        self.test_activity_result = Activity_Result(patient = self.test_patient, solution = self.test_solution, is_correct = False, is_completed = True)
        self.test_activity_result.save()

    def test_activity_result_creation(self):
       activity_result_test = self.test_activity_result

       self.assertEquals(activity_result_test.is_correct, False)
       self.assertEquals(activity_result_test.is_completed, True)

    def tearDown(self):
        self.test_activity_result.delete()
        self.test_solution.delete()
        self.test_activity.delete()
        self.test_patient.delete()
        self.test_doctor.delete()
        self.test_user2.delete()
        self.test_user1.delete()

class PatientTrainingModelTest(TestCase):

    def setUp(self):
        self.test_user1 =  User(is_medic = True, is_patient = False, username="username1", first_name = 'User Test', last_name = 'Model Test 1', comments = 'This is a test', save_session = False)
        self.test_user1.save()
        self.test_doctor = Doctor(user = self.test_user1, specialty = 'Cirujano')
        self.test_doctor.save()
        self.test_user2 =  User(is_medic = False, is_patient = True, username="username2", first_name = 'User Test', last_name = 'Model Test 2', comments = 'This is a test', save_session = False)
        self.test_user2.save()
        self.test_patient = Patient(doctor = self.test_doctor, user = self.test_user2, sickness = 'Alzheimer')    
        self.test_patient.save()
        self.test_training = Training(name = 'Training Test 1', description = 'This is a test', doctor = self.test_doctor)
        self.test_training.save()
        self.test_patient_training = Patient_training(patient = self.test_patient, training = self.test_training, is_completed = True)
        self.test_patient_training.save()

    def test_patient_training_creation(self):
       patient_training_test = self.test_patient_training

       self.assertEquals(patient_training_test.is_completed, True)

    def tearDown(self):
        self.test_patient_training.delete()
        self.test_training.delete()
        self.test_patient.delete()
        self.test_doctor.delete()
        self.test_user2.delete()
        self.test_user1.delete()

class ActivityTrainingModelTest(TestCase):

    def setUp(self):
        self.test_user1 =  User(is_medic = True, is_patient = False, username="username1", first_name = 'User Test', last_name = 'Model Test 1', comments = 'This is a test', save_session = False)
        self.test_user1.save()
        self.test_doctor = Doctor(user = self.test_user1, specialty = 'Cirujano')
        self.test_doctor.save()
        self.test_user2 =  User(is_medic = False, is_patient = True, username="username2", first_name = 'User Test', last_name = 'Model Test 2', comments = 'This is a test', save_session = False)
        self.test_user2.save()
        self.test_patient = Patient(doctor = self.test_doctor, user = self.test_user2, sickness = 'Alzheimer')    
        self.test_patient.save()
        self.test_training = Training(name = 'Training Test 1', description = 'This is a test', doctor = self.test_doctor)
        self.test_training.save()
        self.test_patient_training = Patient_training(patient = self.test_patient, training = self.test_training, is_completed = True)
        self.test_patient_training.save()
        self.test_activity =  Activity(name = 'Test Activity 1', title = 'Title Test Activity', description = 'This is a test')
        self.test_activity.save()
        self.test_activity_training = Activity_Training(patient_training = self.test_patient_training, activity = self.test_activity, name = 'Test Activity Training', is_correct = True, is_completed= True)

    def test_activity_training_creation(self):
       activity_training_test = self.test_activity_training

       self.assertEquals(activity_training_test.is_completed, True)
       self.assertEquals(activity_training_test.is_correct, True)
       self.assertEquals(activity_training_test.name, 'Test Activity Training')

    def tearDown(self):
        self.test_patient_training.delete()
        self.test_training.delete()
        self.test_patient.delete()
        self.test_doctor.delete()
        self.test_user2.delete()
        self.test_user1.delete()


    