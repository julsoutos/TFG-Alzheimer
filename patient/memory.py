from django.shortcuts import render
import urllib.request
from principal.models import User, Activity_Result, Activity_Training, Training, Activity, Solution, Patient
from datetime import datetime
from principal.utils import get_user_by_token
from .utils import get_solution, evaluate
import random
# Create your views here.

path_memory = 'activities/memory/'

#Carga de todas la actividades de la categoría memoria
def memory(request):

    activities = Activity.objects.filter(category="Memory")
    
    context = {'activities' : activities}
    
    return render(request, path_memory +'memory.html', context)



#Pantalla inicio actividad (explicación)
def init_memory(request):
    
    try:
        activity = Activity.objects.get(name = request.GET['activity'])
    except:
        activities = Activity.objects.filter(category="Memory")
        context = {'activities' : activities}
        return render(request, path_memory + 'memory.html', context)

    context = { 'load': False, 'solution':get_solution(request,activity).name, 'name': activity.name}

    return render(request, path_memory + activity.name + '.html', context)


#Carga de los elementos que componen la actividad
def load_memory(request):

    if request.method  == 'POST':
        solution = Solution.objects.get(name = request.GET['activity'])
        user = User.objects.get(username=get_user_by_token(request))
        patient = Patient.objects.get(user=user)
        answer = evaluate(request, solution)
        activity_result = Activity_Result.objects.create(solution=solution, is_correct=answer, patient=patient, is_completed=True)
        activity_result.save()
        
        return render(request, "patient_home.html")
    else:
        try:
            activity = Activity.objects.get(name = request.GET['name'])
            solution = Solution.objects.get(name = request.GET['activity'])
        except:
            activities = Activity.objects.filter(category="Memory")
            context = {'activities' : activities}
            return render(request, path_memory + 'memory.html', context)
    
    context = { 'load': True, 'solution':solution.name }

    return render(request, path_memory + activity.name + '.html', context)



  