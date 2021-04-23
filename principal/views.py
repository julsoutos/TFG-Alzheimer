from django.shortcuts import render
import urllib.request
# Create your views here.

def inicio(request):
    return render(request, 'index.html')