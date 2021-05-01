from django.shortcuts import render
import urllib.request
# Create your views here.
def inicio(request):
    asd = "123"
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')