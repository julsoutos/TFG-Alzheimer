from django.urls import include, path
from . import views




urlpatterns = [
      path('doctor_home/', views.doctor_home, name="doctor_home")
]