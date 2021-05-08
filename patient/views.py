from django.shortcuts import render
import urllib.request
from principal.models import User
from datetime import datetime
from principal.utils import get_user_by_token
# Create your views here.


def patient_home(request):
    user = User.objects.get(username=get_user_by_token(request))
    context = {'user':user}
   
    return render(request, 'patient_home.html', context)

def patient_profile(request):
    user = User.objects.get(username=get_user_by_token(request))
    age = birth(user.birth_date)
    context = {'user':user, 'age': age}
    
    return render(request, 'patient_profile.html', context)

def activities(request):
    return render(request, 'activities.html')

def birth(birth_date):
    return int((datetime.now().date() - birth_date).days / 365.25)
