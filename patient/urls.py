from django.urls import include, path
from . import views
from . import memory
from . import training



urlpatterns = [

      path('patient_home', views.patient_home, name="patient_home"),
      path('patient_profile', views.patient_profile, name="patient_profile"),
      path('activities', views.activities, name="activities"),

      #Activities 
            
            #Memory
            path('memory', memory.memory, name="memory"),
            path('init_memory', memory.init_memory, name="init_memory"),
            path('load_memory', memory.load_memory, name="load_memory"),

            #Attention
            
      path('prueba/', training.prueba, name="prueba")


]