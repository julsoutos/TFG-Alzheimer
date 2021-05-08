from django.shortcuts import render
import urllib.request
from principal.models import User, Activity_Result, Activity_Training, Training, Activity, Solution, Patient
from datetime import datetime
from principal.utils import get_user_by_token
import random
# Create your views here.

path_memory = 'activities/memory/'

#Carga de todas la actividades de la categoría memoria
def memory(request):
    activities = Activity.objects.filter(category="Memory")
    
    context = {'activities' : activities}
    
    return render(request, path_memory +'memory.html', context)



#Pantalla inicio actividad (explicación)
def init_activity(request):

    try:
        activity = Activity.objects.get(name = request.GET['activity'])
    except:
        return render(request, path_memory + 'memory.html')

    context = { 'load': False, 'solution':get_solution(request,activity).name, 'name': activity.name}

    return render(request, path_memory + activity.name + '.html', context)


#Carga de los elementos que componen la actividad
def load_activity(request):

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

            return render(request, path_memory + 'memory.html')
    
    context = { 'load': True, 'solution':solution.name }

    return render(request, path_memory + activity.name + '.html', context)



def get_solution(request, activity):
    solution = list(Solution.objects.filter(activity=activity))
    r = random.randint(0, len(solution) - 1)
    
    return solution[r]



def evaluate(request, solution):

    expected_solution = list(Solution.objects.filter(name = solution))[0] 
    answer = request.POST['answer']

    return True if expected_solution.solution == answer else False
     


import logging
def prueba(request):
    training = Training.objects.get(pk=1)
    activities = Activity_Training.objects.filter(training=1, isCompleted=False)
    if request.method == 'POST':
        n = request.POST
        activity = list(n.items())[1]
        a = Activity_Training.objects.get(activity = activity)
        a.isCompleted = True
        a.save()
        
    if not activities:
        training.isCompleted = True
        training.save()
        return render(request, 'patient_home.html')
        
    context = { 'activity': activities[0] }
   
    return render(request, path_memory +'prueba.html', context)
  