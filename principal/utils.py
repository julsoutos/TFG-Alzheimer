from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render


def isLogged(request):

    context = {
        "logged":False
    }

    if request.COOKIES.get("cognitya") and request.user.username != "" and valid_token(request.user, request.COOKIES.get("cognitya") ):
        tk = get_object_or_404(Token, key=request.COOKIES.get("cognitya"))
        if tk.user and tk.user.is_authenticated and tk.user == request.user:
            context["logged"] = True


    return context

def valid_token(user, token):
    res = False
    try:
        user_token = get_object_or_404(Token, user=user)
        expected_token = get_object_or_404(Token, key=token)
        if user_token == expected_token:
            res = True
    except:
        res = False
    return res
            
def deleted_valid_token(request):
    response = None
    try:
        if request.user.username != "" and not request.COOKIES.get("cognitya") and get_object_or_404(Token, user=request.user):
            response = redirect("/")
            response.set_cookie("cognitya", get_object_or_404(Token, user=request.user))
    except:
        response = None
    return response

def get_user_token(user):
    token = None
    try:
        if user.username != "":
            token = get_object_or_404(Token, user=user)
    except:
        token = None
    return token
