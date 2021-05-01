from django.shortcuts import render
import urllib.request
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from principal.models import User, Doctor, Patient
from .forms import CreateDoctorForm, CreatePatientForm
import logging


# Create your views here.

def form_doctor(request):
    form  = CreateDoctorForm()
    if request.method == 'POST':
        doctor_form = CreateDoctorForm(request.POST,"form")
        if doctor_form.is_valid():
            username = doctor_form.cleaned_data['username']
            password = doctor_form.cleaned_data['password']
            first_name = doctor_form.cleaned_data['first_name']
            last_name = doctor_form.cleaned_data['last_name']
            birth_date = doctor_form.cleaned_data['birth_date']
            comments = doctor_form.cleaned_data['comments']
            specialty = doctor_form.cleaned_data['specialty']
            email = doctor_form.cleaned_data['email']
            
            user = User.objects.create(username=username, password=password , first_name=first_name, last_name=last_name, birth_date=birth_date, comments=comments, is_medic=True, email=email)
            user.set_password(password)
            user.save()

            doctor = Doctor.objects.create(user=user ,specialty=specialty)
            doctor.save()

    context = {'form':form}

    return render(request, 'create_doctor.html', context)

def form_patient(request):
    form  = CreatePatientForm()
    if request.method == 'POST':
        patient_form = CreatePatientForm(request.POST,"form")
        if patient_form.is_valid():
            username = patient_form.cleaned_data['username']
            password = patient_form.cleaned_data['password']
            first_name = patient_form.cleaned_data['first_name']
            last_name = patient_form.cleaned_data['last_name']
            birth_date = patient_form.cleaned_data['birth_date']
            comments = patient_form.cleaned_data['comments']
            sickness = patient_form.cleaned_data['sickness']
            email = patient_form.cleaned_data['email']
            
            user = User.objects.create(username=username, password=password , first_name=first_name, last_name=last_name, birth_date=birth_date, comments=comments, is_patient=True, email=email)
            user.set_password(password)
            user.save()

            patient = Patient.objects.create(user=user ,sickness=sickness)
            patient.save()

    context = {'form':form}

    return render(request, 'create_patient.html', context)