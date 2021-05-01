from django.urls import include, path
from . import views




urlpatterns = [
    path('login_form/', views.login_form, name="login_form"),
    path('account/', views.account, name="account"),
    path('prueba/', views.prueba, name="prueba")

]