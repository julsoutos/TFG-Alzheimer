from django.shortcuts import render
import urllib.request
from .utils import isLogged
# Create your views here.

def inicio(request):
    return render(request, 'index.html', isLogged(request))

def about(request):
    return render(request, 'about.html', isLogged(request))