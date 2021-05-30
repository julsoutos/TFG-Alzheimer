from django.urls import include, path
from . import views




urlpatterns = [
      path('form_doctor', views.form_doctor, name="form_doctor"),
      path('form_patient', views.form_patient, name="form_patient"),
      path('admin_home', views.admin_home, name="admin_home"),
      path('user_types', views.user_types, name="user_types"),
      path('all_patients', views.all_patients, name="all_patients"),
      path('all_doctors', views.all_doctors, name="all_doctors"),         
      path('delete_user', views.delete_user, name="delete_user"),         

]