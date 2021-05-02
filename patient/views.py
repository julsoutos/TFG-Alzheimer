from django.shortcuts import render
import urllib.request

# Create your views here.

def patient_home(request):
    return render(request, 'patient_home.html')

