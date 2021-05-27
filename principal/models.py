from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

class User(AbstractUser):

    is_medic = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(max_length=100, null=True)
    comments = models.CharField(max_length=400)
    save_session = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sickness = models.CharField(max_length=300)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

class Activity(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(default="Title", max_length=100)
    ACTIVITY_CATEGORY = (
    ('None','None'),    
    ('Memory','Memoria'),
    ('Attention','Atencion'),
    ('Calculus','Cálculo'),
    ('Perception','Percepción'),
    ('Language','Lenguaje'),
    )
    description = models.TextField(default="Activity")
    category = models.CharField( max_length=10,choices=ACTIVITY_CATEGORY, default="None")
    def __str__(self):
        return self.name

class Solution(models.Model):
    name = models.CharField(max_length=100, default="")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    solution = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default="Training")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
 

    def __str__(self):
        return self.name



class Activity_Result(models.Model):
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    end_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.solution.name


class Patient_training(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.patient.user.username + ' - ' + self.training.name


class Activity_Training(models.Model):
    name = models.CharField(max_length=100)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    patient_training = models.ForeignKey(Patient_training, on_delete=models.CASCADE, null=True)
    is_completed = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return self.activity.name + " - " + self.patient_training.training.name