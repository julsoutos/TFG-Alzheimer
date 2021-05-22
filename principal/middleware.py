from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .utils import isLogged, deleted_valid_token , valid_token, get_user_token
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from datetime import datetime
import pytz

class Interceptor:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kargs):
        response = HttpResponse("User Permissions")
        path = request.path_info.lstrip("/")

        #Si el usuario es anónimo e intenta acceder a urls de usuario autenticado, se redige a la página de inicio
        if isLogged(request)["logged"] == False and path and not "authentication" in path and not "principal" in path :        
            response = redirect(to="inicio")
            return response

        #Si la cookie se ha eliminido y existe un token de sesión registrado para el usuario, se asigna la cookie del token correspondiente
        if deleted_valid_token(request) is not None:
            response = deleted_valid_token(request)
            return response

        #Si el token no es válido y el usuario tiene un token de sesión registrado, se asigna la cookie con el token correspondiente
        if not valid_token(request.user, request.COOKIES.get("cognitya")) and request.user.username != "" and get_user_token(request.user) is not None:
            response = redirect(to="inicio")
            response.set_cookie("cognitya", get_object_or_404(Token, user=request.user))
            return response
        
        #Si se inserta una cookie en el navegador y el usuario no tiene resgistrado ningún token en la base de datos, se elimina la cookie correspondiente
        if request.COOKIES.get("cognitya") and get_user_token(request.user) is None:
            response = redirect(to="inicio")
            response.delete_cookie("cognitya")
            return response

        #Si el token ha expirado (10 horas), se elimina el token y la cookie
        if valid_token(request.user, request.COOKIES.get("cognitya")):
            tk = get_object_or_404(Token, key=request.COOKIES.get("cognitya"))
            n = datetime.utcnow().replace(tzinfo=pytz.UTC) - tk.created
            print(n.total_seconds())
            if n.total_seconds() >= 36000 and not "/authentication/logout" in request.path and request.user.save_session == False:
                response = redirect(to="/authentication/logout")
                return response

        
        

     
        
            
