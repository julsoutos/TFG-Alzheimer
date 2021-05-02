from django.shortcuts import render
import urllib.request

# Create your views here.

def doctor_home(request):
    return render(request, 'doctor_home.html')

