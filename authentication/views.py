from django.shortcuts import render, redirect
import urllib.request
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from principal.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


# Create your views here.

def login_form(request):
    return render(request, 'login.html')


def account(request):
    response = HttpResponse('Login Error')
    response = redirect(to="inicio")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) 
            try: 
                if get_object_or_404(Token, user=user):
                    tk = get_object_or_404(Token, user=user)
                    tk.delete() 
            except:
               pass

            token = Token.objects.create(user=user)
            response = HttpResponse('Login Sucessfully')
            response = redirect(to=type_user(user))
            response.set_cookie('cognitya', token)
            if(request.POST.get('save_session')):
                token.user.save_session = True
                token.user.save()

            
    return response

def type_user(user):
    if user.is_patient:
        return "patient_home"
    if user.is_medic:
        return "doctor_home"
    else:
        return "admin_home"





def user_logout(request):

    response = HttpResponse('Logout')
  
    key = request.COOKIES.get("cognitya")
    tk = get_object_or_404(Token, key=key)
    user = tk.user
    tk.user.save_session = False
    tk.user.save()
   
    tk.delete()
    logout(request)
    
    response = redirect(to="inicio")
    response.delete_cookie('cognitya')

    return response