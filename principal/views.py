from principal.models import User
from django.shortcuts import redirect, render
from .utils import isLogged, get_user_by_token
from authentication.views import type_user
# Create your views here.

def inicio(request):
    return render(request, 'index.html', isLogged(request))

def about(request):
    return render(request, 'about.html', isLogged(request))

def error_404(request, exception):
    context = {'error': '404'}
    return render(request, '404.html', context)

def comeback(request):
    try:
        user = User.objects.get(username=get_user_by_token(request))
        return redirect(to=type_user(user))
    except:
        return redirect(to=inicio)