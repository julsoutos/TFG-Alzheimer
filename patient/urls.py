from django.urls import include, path
from . import views
from . import activity
from . import training



urlpatterns = [

      path('patient_home', views.patient_home, name="patient_home"),
      path('patient_profile', views.patient_profile, name="patient_profile"),
      path('activities', views.activities, name="activities"),

      #Activities 
            
            path('activity', activity.activity, name="activity"),
            path('init_activity', activity.init_activity, name="init_activity"),
            path('load_activity', activity.load_activity, name="load_activity"),

      

      #Trainings
            path('list_trainings', training.list_trainings, name="list_trainings"),

            path('init_training', training.init_training, name="init_training"),

            path('load_training', training.load_training, name="load_training")


]