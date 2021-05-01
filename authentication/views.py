from django.shortcuts import render
import urllib.request
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from principal.models import User
from rest_framework.authtoken.models import Token


# Create your views here.

def login_form(request):
    return render(request, 'login.html')

import logging
def account(request):
    response = HttpResponse('Login Error')
    response = render(request, 'index.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # new_user = User.objects.create_user(username)
        # new_user.set_password(password)
        # new_user.save()
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)        
            token = Token.objects.create(user=user)
            response = HttpResponse('Login Sucessfully')
            response = render(request, 'prueba.html')
            response.set_cookie('cognitya', token, max_age=36000)
            
            if(request.POST.get('save_session')):
                response.set_cookie('cognitya', token)

            
    return response

def prueba(request):
    logging.warning(request.COOKIES.get('cognitya'))
    return render(request, 'prueba.html')
