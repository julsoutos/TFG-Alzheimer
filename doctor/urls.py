from django.urls import path
from . import views




urlpatterns = [
      path('doctor_home', views.doctor_home, name="doctor_home"),

      path('patients', views.patients, name="patients"),

      path('trainings', views.trainings, name="trainings"),

      path('training_details', views.training_details, name="training_details"),

      path('create_training', views.create_training, name="create_training")


]