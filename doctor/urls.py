from django.urls import path
from . import views, stats




urlpatterns = [
      
      path('doctor_home', views.doctor_home, name="doctor_home"),

      path('patients', views.patients, name="patients"),

      path('patient_details', views.patient_details, name="patient_details"),

      path('patient_stats', stats.patient_stats, name="patient_stats"),

      path('trainings', views.trainings, name="trainings"),

      path('list_activities', views.activities, name="list_activities"),

      path('activity_details', views.activity_details, name="activity_details"),

      path('training_details', views.training_details, name="training_details"),

      path('delete_training', views.delete_training, name="delete_training"),

      path('create_training', views.create_training, name="create_training"),

      path('trainings_completed', views.trainings_completed, name="trainings_completed"),

      path('training_stats', stats.training_stats, name="training_stats"),

      path('list_test', views.tests, name="list_test"),



]