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
from principal.models import  Doctor, User, Patient
import datetime

class AdminTestCreatePatient(StaticLiveServerTestCase):

    def create_admin(self):
        self.admin = User(username="test_admin", first_name="Admin", is_staff=True)
        self.admin.set_password("test_admin")
        self.admin.save()

    def create_doctor(self):
        self.user1 = User(username="test_doctor", first_name="Doctor", is_medic=True)
        self.user1.set_password("test_doctor")
        self.user1.save()

        self.doctor = Doctor(specialty="Test specialty", user=self.user1)
        self.doctor.save()

    def setUp(self):

        self.create_admin()
        self.create_doctor()

        self.vars = {}
        settings.DEBUG = True
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
                
        super().setUp()

    def test_create_patient(self):
        self.driver.get(f'{self.live_server_url}/authentication/login_form')
        self.driver.set_window_size(1166, 936)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test_admin")
        self.driver.find_element(By.ID, "id_password").send_keys("test_admin")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".bx-user").click()
        time.sleep(3)
    
        element = self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) .mb-1")
        self.driver.execute_script("arguments[0].click();", element)
        
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("test patient")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("test patient")
        self.driver.find_element(By.ID, "id_first_name").click()
        self.driver.find_element(By.ID, "id_first_name").send_keys("test patient")
        self.driver.find_element(By.ID, "id_last_name").click()
        self.driver.find_element(By.ID, "id_last_name").send_keys("test patient")
        self.driver.find_element(By.ID, "id_address").click()
        self.driver.find_element(By.ID, "id_address").send_keys("test patient")
        self.driver.find_element(By.ID, "id_city").click()
        self.driver.find_element(By.ID, "id_city").send_keys("test patient")
        self.driver.find_element(By.ID, "id_sickness").click()
        self.driver.find_element(By.ID, "id_sickness").send_keys("test patient")
        self.driver.find_element(By.ID, "id_birth_date").click()
        self.driver.find_element(By.ID, "id_birth_date").send_keys("29-03-1977")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys("prodriguezgarrido11@gmail.com")
        self.driver.find_element(By.ID, "id_doctor").send_keys("test_doctor")
        self.driver.find_element(By.ID, "id_comments").send_keys("test comments")
        
        time.sleep(3)      

        element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
        self.driver.execute_script("arguments[0].click();", element)
        
        time.sleep(3)
        logging.warning(self.driver.current_url)
        assert self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text == "test patient"


    def tearDown(self):
        self.driver.quit()

        self.admin.delete()
        self.user1.delete()
        self.doctor.delete()
       

        super().tearDown()


# class AdminTestCreateDoctor(StaticLiveServerTestCase):

#     def create_admin(self):
#         self.admin = User(username="test_admin", first_name="Admin", is_staff=True)
#         self.admin.set_password("test_admin")
#         self.admin.save()


#     def setUp(self):

#         self.create_admin()

#         self.vars = {}
#         settings.DEBUG = True
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)
                
#         super().setUp()
    

#     def test_create_doctor(self):
#         self.driver.get(f'{self.live_server_url}/authentication/login_form')
#         self.driver.set_window_size(1166, 936)
#         self.driver.find_element(By.ID, "id_username").click()
#         self.driver.find_element(By.ID, "id_username").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
#         time.sleep(3)
#         self.driver.find_element(By.CSS_SELECTOR, ".bx-user").click()
#         time.sleep(3)
    
#         element = self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2) .mb-1")
#         self.driver.execute_script("arguments[0].click();", element)
        
#         time.sleep(3)

#         self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
#         self.driver.find_element(By.ID, "id_username").click()
#         self.driver.find_element(By.ID, "id_username").send_keys("test doctor")
#         self.driver.find_element(By.ID, "id_password").click()
#         self.driver.find_element(By.ID, "id_password").send_keys("test doctor")
#         self.driver.find_element(By.ID, "id_first_name").click()
#         self.driver.find_element(By.ID, "id_first_name").send_keys("test doctor")
#         self.driver.find_element(By.ID, "id_last_name").click()
#         self.driver.find_element(By.ID, "id_last_name").send_keys("test doctor")
#         self.driver.find_element(By.ID, "id_specialty").click()
#         self.driver.find_element(By.ID, "id_specialty").send_keys("test specialty")
#         self.driver.find_element(By.ID, "id_birth_date").click()
#         self.driver.find_element(By.ID, "id_birth_date").send_keys("29-03-1977")
#         self.driver.find_element(By.ID, "id_email").click()
#         self.driver.find_element(By.ID, "id_email").send_keys("prodriguezgarrido11@gmail.com")
#         self.driver.find_element(By.ID, "id_comments").click()
#         self.driver.find_element(By.ID, "id_comments").send_keys("test comments")
#         time.sleep(3)      

#         element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
#         self.driver.execute_script("arguments[0].click();", element)
        
#         time.sleep(8)
#         assert self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text == "test doctor test doctor"

    
#     def tearDown(self):
#         self.driver.quit()

#         self.admin.delete()
       
#         super().tearDown()


# class AdminTestEditPatient(StaticLiveServerTestCase):


#     def create_admin(self):
#         self.admin = User(username="test_admin", first_name="Admin", is_staff=True)
#         self.admin.set_password("test_admin")
#         self.admin.save()

#     def create_doctor(self):
#         self.user1 = User(username="test_doctor", first_name="Doctor", is_medic=True)
#         self.user1.set_password("test_doctor")
#         self.user1.save()

#         self.doctor = Doctor(specialty="Test specialty", user=self.user1)
#         self.doctor.save()

#     def create_patient(self):
#         date1 = datetime.datetime.today().date()
#         date2 = date1 - datetime.timedelta(days=20)

#         self.user = User(username="test_patient", first_name="patient", last_name="patient", email="example@gmail.com", is_patient=True, birth_date=date2)
#         self.user.set_password("test_patient")
#         self.user.save()
        
#         self.patient = Patient(sickness="test_patient", user=self.user, doctor=self.doctor, address="Test location", city="Test city")
#         self.patient.save()




#     def setUp(self):

#         self.create_admin()
#         self.create_doctor()
#         self.create_patient()

#         self.vars = {}
#         settings.DEBUG = True
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)
                
#         super().setUp()


#     def test_edit_patient(self):
#         self.driver.get(f'{self.live_server_url}/authentication/login_form')
#         self.driver.set_window_size(1166, 936)
#         self.driver.find_element(By.ID, "id_username").click()
#         self.driver.find_element(By.ID, "id_username").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
#         time.sleep(3)
#         self.driver.find_element(By.CSS_SELECTOR, ".bx-user").click()
#         time.sleep(3)
    
#         self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) .mb-1").click()
       
#         time.sleep(3)
#         element = self.driver.find_element(By.CSS_SELECTOR, "td > .btn:nth-child(1)") 
#         self.driver.execute_script("arguments[0].click();", element)
#         time.sleep(3)
#         self.driver.find_element(By.ID, "id_first_name").click()
#         self.driver.find_element(By.ID, "id_first_name").send_keys("2")
    
#         self.driver.find_element(By.ID, "id_last_name").click()
#         self.driver.find_element(By.ID, "id_last_name").send_keys("2")

#         self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
#         time.sleep(3)

#         self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").click()
#         assert self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text == "patient2"
#         self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2)").click()
#         assert self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text == "patient2"




#     def tearDown(self):
#         self.driver.quit()

#         self.admin.delete()
#         self.user.delete()
#         self.user1.delete()
#         self.doctor.delete()
#         self.patient.delete()



#         super().tearDown()


# class AdminTestEditDoctor(StaticLiveServerTestCase):


#     def create_admin(self):
#         self.admin = User(username="test_admin", first_name="Admin", is_staff=True)
#         self.admin.set_password("test_admin")
#         self.admin.save()

#     def create_doctor(self):
#         date1 = datetime.datetime.today().date()
#         date2 = date1 - datetime.timedelta(days=20)
#         self.user = User(username="test_doctor", first_name="doctor", last_name="doctor", email="example@gmail.com", is_medic=True, birth_date=date2)
#         self.user.set_password("test_doctor")
#         self.user.save()

#         self.doctor = Doctor(specialty="Test specialty", user=self.user)
#         self.doctor.save()

  
#     def setUp(self):

#         self.create_admin()
#         self.create_doctor()

#         self.vars = {}
#         settings.DEBUG = True
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)
                
#         super().setUp()


#     def test_edit_doctor(self):
#         self.driver.get(f'{self.live_server_url}/authentication/login_form')
#         self.driver.set_window_size(1166, 936)
#         self.driver.find_element(By.ID, "id_username").click()
#         self.driver.find_element(By.ID, "id_username").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
#         time.sleep(3)
#         self.driver.find_element(By.CSS_SELECTOR, ".bx-user").click()
#         time.sleep(3)
    
#         self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2) .mb-1").click()
       
#         time.sleep(3)
#         element = self.driver.find_element(By.CSS_SELECTOR, "td > .btn:nth-child(1)") 
#         self.driver.execute_script("arguments[0].click();", element)
#         time.sleep(3)
#         self.driver.find_element(By.ID, "id_first_name").click()
#         self.driver.find_element(By.ID, "id_first_name").send_keys("2")
    
#         self.driver.find_element(By.ID, "id_last_name").click()
#         self.driver.find_element(By.ID, "id_last_name").send_keys("2")

#         self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
#         time.sleep(3)

#         self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").click()
#         assert self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text == "doctor2 doctor2"
     

#     def tearDown(self):
#         self.driver.quit()

#         self.admin.delete()
#         self.user.delete()
#         self.doctor.delete()

#         super().tearDown()

# class AdminTestDeleteDoctor(StaticLiveServerTestCase):

#     def create_admin(self):
#         self.admin = User(username="test_admin", first_name="Admin", is_staff=True)
#         self.admin.set_password("test_admin")
#         self.admin.save()

#     def create_doctor(self):
#         date1 = datetime.datetime.today().date()
#         date2 = date1 - datetime.timedelta(days=20)
#         self.user = User(username="test_doctor", first_name="doctor", last_name="doctor", email="example@gmail.com", is_medic=True, birth_date=date2)
#         self.user.set_password("test_doctor")
#         self.user.save()

#         self.doctor = Doctor(specialty="Test specialty", user=self.user)
#         self.doctor.save()

  
#     def setUp(self):

#         self.create_admin()
#         self.create_doctor()

#         self.vars = {}
#         settings.DEBUG = True
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)
                
#         super().setUp()


#     def test_delete_doctor(self):
#         self.driver.get(f'{self.live_server_url}/authentication/login_form')
#         self.driver.set_window_size(1166, 936)
#         self.driver.find_element(By.ID, "id_username").click()
#         self.driver.find_element(By.ID, "id_username").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
#         time.sleep(3)
#         self.driver.find_element(By.CSS_SELECTOR, ".bx-user").click()
#         time.sleep(3)
    
#         self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2) .mb-1").click()
       
#         time.sleep(3)
#         element = self.driver.find_element(By.CSS_SELECTOR, "td > .btn:nth-child(2)") 
#         self.driver.execute_script("arguments[0].click();", element)
#         time.sleep(3)
       
       
#         assert len(self.driver.find_elements(By.CSS_SELECTOR, "td:nth-child(1)")) == 0
        
     

#     def tearDown(self):
#         self.driver.quit()

#         self.admin.delete()
#         self.user.delete()
#         self.doctor.delete()

#         super().tearDown()

# class AdminTestDeletePatient(StaticLiveServerTestCase):

#     def create_admin(self):
#         self.admin = User(username="test_admin", first_name="Admin", is_staff=True)
#         self.admin.set_password("test_admin")
#         self.admin.save()

#     def create_doctor(self):
#         self.user1 = User(username="test_doctor", first_name="Doctor", is_medic=True)
#         self.user1.set_password("test_doctor")
#         self.user1.save()

#         self.doctor = Doctor(specialty="Test specialty", user=self.user1)
#         self.doctor.save()

#     def create_patient(self):
#         date1 = datetime.datetime.today().date()
#         date2 = date1 - datetime.timedelta(days=20)

#         self.user = User(username="test_patient", first_name="patient", last_name="patient", email="example@gmail.com", is_patient=True, birth_date=date2)
#         self.user.set_password("test_patient")
#         self.user.save()
        
#         self.patient = Patient(sickness="test_patient", user=self.user, doctor=self.doctor, address="Test location", city="Test city")
#         self.patient.save()




#     def setUp(self):

#         self.create_admin()
#         self.create_doctor()
#         self.create_patient()

#         self.vars = {}
#         settings.DEBUG = True
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)
                
#         super().setUp()


#     def test_delete_patient(self):
#         self.driver.get(f'{self.live_server_url}/authentication/login_form')
#         self.driver.set_window_size(1166, 936)
#         self.driver.find_element(By.ID, "id_username").click()
#         self.driver.find_element(By.ID, "id_username").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys("test_admin")
#         self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
#         time.sleep(3)
#         self.driver.find_element(By.CSS_SELECTOR, ".bx-user").click()
#         time.sleep(3)
    
#         self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) .mb-1").click()
       
#         time.sleep(3)
#         element = self.driver.find_element(By.CSS_SELECTOR, "td > .btn:nth-child(2)") 
#         self.driver.execute_script("arguments[0].click();", element)
#         time.sleep(3)
       
       
#         assert len(self.driver.find_elements(By.CSS_SELECTOR, "td:nth-child(1)")) == 0




#     def tearDown(self):
#         self.driver.quit()

#         self.admin.delete()
#         self.user.delete()
#         self.user1.delete()
#         self.doctor.delete()
#         self.patient.delete()



#         super().tearDown()