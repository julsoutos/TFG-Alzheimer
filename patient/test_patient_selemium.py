from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time
from django.conf import settings
from principal.models import Activity_Training, Doctor, Mental_Test, Patient_training, Solution, Test_Result, Training, User, Activity, Patient


class PatientTest(StaticLiveServerTestCase):

    def create_patient(self):
        self.user1 = User(username="test_patient", is_patient=True)
        self.user1.set_password("test_patient")
        self.user1.save()
        
        self.patient = Patient(sickness="test_patient", user=self.user1)
        self.patient.save()

    def create_activity(self):
        self.activity = Activity(name="Image Order", title="Recuerda el orden de las imágenes", description="Activity",
                                category="Memory")
        self.activity.save()

        self.solution = Solution(name="Image Order 1", activity=self.activity, solution=3)
        
        self.solution.save()
          

    def create_doctor(self):
        self.user2 = User(username="test_doctor", first_name="Doctor", is_medic=True)
        self.user2.set_password("test_doctor")
        self.user2.save()

        self.doctor = Doctor(specialty="Test specialty", user=self.user2)
        self.doctor.save()

    def create_training(self):
        self.training = Training(name="Test training", doctor=self.doctor)
        self.training.save()

        self.patient_training = Patient_training(training=self.training, patient=self.patient)
        self.patient_training.save()

        self.activity_training = Activity_Training(name="", activity=self.activity, patient_training=self.patient_training)
        self.activity_training.save()

        self.test = Mental_Test(name="Isaac Test")
        self.test.save()

        self.test_result = Test_Result(patient_training=self.patient_training, mental_Test=self.test)
        self.test_result.save()
          
    def setUp(self):

        self.create_patient()
        self.create_activity()
        self.create_doctor()
        self.create_training()

        self.vars = {}
        settings.DEBUG = True
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
                
        super().setUp()



    def tearDown(self):
        self.driver.quit()
        self.user1.delete()
        self.user2.delete()

        self.patient.delete()
        self.doctor.delete()
        self.activity.delete()
        self.solution.delete()

        self.training.delete()
        self.patient_training.delete()
        self.activity_training.delete()
        self.test.delete()
        self.test_result.delete()

        super().tearDown()

    def test_do_activity(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_patient")
        self.driver.find_element(By.ID, "id_password").send_keys("test_patient")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(2) .img-fluid").click()
        self.driver.find_element(By.CSS_SELECTOR, ".blue span").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) .btn-buy").click()
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(3)

        self.driver.find_element(By.ID, "1").click()
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, ".btn-buy").click()
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, "h3").click()
        time.sleep(3)

        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "¡Actividad completada!"
        self.driver.find_element(By.LINK_TEXT, "Volver al inicio").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "ACCIONES DISPONIBLES"
    
    def test_do_training(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.ID, "id_username").send_keys("test_patient")
        self.driver.find_element(By.ID, "id_password").send_keys("test_patient")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Entrenamiento").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-1:nth-child(2)").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Comenzar").click()
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(3)

        self.driver.find_element(By.ID, "1").click()

        self.driver.find_element(By.CSS_SELECTOR, ".btn-buy").click()
        time.sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Siguiente").click()
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(3)

        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-buy:nth-child(7)")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Siguiente").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "¡Entrenamiento completado!"

        self.driver.find_element(By.LINK_TEXT, "Volver al inicio").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "ACCIONES DISPONIBLES"