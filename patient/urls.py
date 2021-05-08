from django.urls import include, path
from . import views
from . import memory



urlpatterns = [
      path('patient_home/', views.patient_home, name="patient_home"),
      path('patient_profile/', views.patient_profile, name="patient_profile"),
      path('activities/', views.activities, name="activities"),

      #Activities
      path('memory/', memory.memory, name="memory"),
      path('init_activity/', memory.init_activity, name="init_activity"),
      path('load_activity/', memory.load_activity, name="load_activity"),

      path('prueba/', memory.prueba, name="prueba")


]