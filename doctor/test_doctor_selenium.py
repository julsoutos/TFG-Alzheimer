import logging
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time
from django.conf import settings
from principal.models import  Doctor, Mental_Test, User, Activity, Patient
import datetime

class DoctorTest(StaticLiveServerTestCase):

    def create_doctor(self):
        self.user1 = User(username="test_doctor", first_name="Doctor", is_medic=True)
        self.user1.set_password("test_doctor")
        self.user1.save()

        self.doctor = Doctor(specialty="Test specialty", user=self.user1)
        self.doctor.save()

    def create_patient(self):
        date1 = datetime.datetime.today().date()
        date2 = date1 - datetime.timedelta(days=20)

        logging.warning(date2)
        self.user2 = User(username="test_patient", first_name="patient", is_patient=True, birth_date=date2)
        self.user2.set_password("test_patient")
        self.user2.save()
        
        self.patient = Patient(sickness="test_patient", user=self.user2, doctor=self.doctor)
        self.patient.save()

    def create_activity(self):
        self.activity = Activity(name="Image Order", title="Recuerda el orden de las imágenes", description="Activity",
                                category="Memory")
        self.activity.save()

    def create_mental_test(self):

        self.test = Mental_Test(name="Isaac Test")
        self.test.save()

                  
    def setUp(self):

        self.create_doctor()
        self.create_patient()
        self.create_activity()
        self.create_mental_test()

        self.vars = {}
        settings.DEBUG = True
        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
                
        super().setUp()

    def tearDown(self):
        self.driver.quit()
        self.user1.delete()
        self.user2.delete()

        self.patient.delete()
        self.doctor.delete()
        self.activity.delete()
        self.test.delete()

        super().tearDown()
    
    def test_create_training(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .bx").click()
        time.sleep(3)

        element = self.driver.find_element(By.ID, "create")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)

        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("training test")
        self.driver.find_element(By.ID, "id_description").click()
        self.driver.find_element(By.ID, "id_description").send_keys("training test")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .create").click()
       
        self.driver.find_element(By.ID, "test_patient").click()
        
        self.driver.find_element(By.CSS_SELECTOR, "#patients .modal-footer > .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) > .create").click()
        self.driver.find_element(By.ID, "Isaac Test").click()
        self.driver.find_element(By.CSS_SELECTOR, "#tests .modal-footer > .btn").click()

        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(4) > .create").click()
        self.driver.find_element(By.ID, "Image Order").click()
        self.driver.find_element(By.CSS_SELECTOR, "#activities .modal-footer > .btn").click()
        
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .create").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(1)").text == "training test"
    
    def test_list_patient(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .bx").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, "tbody th").text == "PATIENT"
    
    def test_patient_details(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .bx").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "legend").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "legend").text == "patient"