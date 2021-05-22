from django.urls import include, path
from . import views




urlpatterns = [
      path('form_doctor/', views.form_doctor, name="form_doctor"),
      path('form_patient/', views.form_patient, name="form_patient"),
      path('admin_home/', views.admin_home, name="admin_home"),
]