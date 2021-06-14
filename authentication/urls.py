from django.urls import include, path
from . import views




urlpatterns = [
    path('login_form',views.login_form, name="login_form"),
    path('logout', views.user_logout, name="user_logout")
]