from django.shortcuts import redirect, render
from .utils import isLogged
# Create your views here.

def inicio(request):
    return render(request, 'index.html', isLogged(request))

def about(request):
    return render(request, 'about.html', isLogged(request))

def error_404(request, exception):
    return render(request, 'index.html')