from django.urls import include, path
from . import views




urlpatterns = [
      path('patient_home/', views.patient_home, name="patient_home")
]