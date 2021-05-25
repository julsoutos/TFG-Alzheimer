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

      path('create_training', views.create_training, name="create_training")


]