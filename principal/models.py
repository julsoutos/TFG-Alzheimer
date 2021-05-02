from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    is_medic = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(max_length=100, null=True)
    comments = models.CharField(max_length=400)
    save_session = models.BooleanField(default=False)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=100)
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sickness = models.CharField(max_length=300)

class Activity(models.Model):
    name = models.CharField(max_length=100)

class Solution(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE, primary_key=True)
    solution = models.CharField(max_length=300)