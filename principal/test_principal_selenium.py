from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time
from django.conf import settings
from .models import User

class LoginTest(StaticLiveServerTestCase):

    def create_patient(self):
        self.patient = User(username="test_patient", is_patient=True)
        self.patient.set_password("test_patient")
        self.patient.save()

    def create_doctor(self):
        self.doctor = User(username="test_doctor", first_name="Doctor", is_medic=True)
        self.doctor.set_password("test_doctor")
        self.doctor.save()
          

    def create_admin(self):
        self.admin = User(username="test_admin", first_name="Admin", is_staff=True)
        self.admin.set_password("test_admin")
        self.admin.save()
          
    def setUp(self):

        self.create_patient()
        self.create_doctor()
        self.create_admin()

        self.vars = {}
        settings.DEBUG = True
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
                
        super().setUp()

    
    def test_login_patient(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_patient")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("test_patient")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(2)
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "ACCIONES DISPONIBLES"

    def test_login_admin(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_admin")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("test_admin")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(2)
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "ADMIN"

    def test_login_admin(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(2)
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "DOCTOR"

    def tearDown(self):
        self.driver.quit()
        self.patient.delete()
        self.doctor.delete()
        self.admin.delete()
        super().tearDown()