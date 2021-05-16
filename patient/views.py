from patient import training
from django.shortcuts import render
import urllib.request
from principal.models import User, Activity_Result, Patient, Patient_training
from datetime import datetime
from principal.utils import get_user_by_token
# Create your views here.


def patient_home(request):
    user = User.objects.get(username=get_user_by_token(request))
    context = {'user':user}
   
    return render(request, 'patient_home.html', context)

def patient_profile(request):

    user = User.objects.get(username=get_user_by_token(request))
    patient = Patient.objects.get(user=user)
    age = birth(user.birth_date)
    activities = Activity_Result.objects.filter(patient=patient, is_completed=True)
    patient_training = Patient_training.objects.filter(patient=patient, is_completed=True)
    not_completed = Patient_training.objects.filter(patient=patient, is_completed=False)



    context = {'user':user, 'age': age, 'activities': activities.count(), 'trainings': patient_training.count(), 'not_completed': not_completed.count()}
    
    return render(request, 'patient_profile.html', context)

def activities(request):
    return render(request, 'activities.html')

def birth(birth_date):
    return int((datetime.now().date() - birth_date).days / 365.25)
