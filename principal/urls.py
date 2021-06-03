from django.urls import include, path
from . import views




urlpatterns = [
      path('about', views.about, name="about"),
      path('comeback', views.comeback, name="comeback")


]