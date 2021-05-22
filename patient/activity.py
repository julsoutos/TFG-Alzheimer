from django.shortcuts import redirect, render
from principal.models import User, Activity_Result, Activity, Solution, Patient
from principal.utils import get_user_by_token
from .utils import get_solution, evaluate
import json
# Create your views here.

path_activity = 'activities/'


#Carga de todas la actividades de la categoría memoria
def activity(request):

    try:

        category = request.GET['category'].replace("'", "").strip()
        
        activities = Activity.objects.filter(category=category)

            
        context = {'activities' : activities} 

        return render(request, path_activity +  category.lower() + '/' +  category.lower() + '.html', context)
    
    except:

        return redirect(to="activities")



#Pantalla inicio actividad (explicación)
def init_activity(request):

    
    activity = Activity.objects.get(name = request.GET['activity'])

    context = { 'load': False, 'solution':get_solution(request,activity), 'activity': activity, 'training': False}

    return render(request,  path_activity+ '/' +  activity.name + '.html', context)


#Carga de los elementos que componen la actividad
def load_activity(request):


    activity = Activity.objects.get(name = request.GET['name'])
    solution = Solution.objects.get(name = request.GET['activity'])

    json_c = {"hola":json.dumps([1,2,3])}

    if request.method  == 'POST':
        user = User.objects.get(username=get_user_by_token(request))
        patient = Patient.objects.get(user=user)
        answer = evaluate(request, solution, 'answer')
        activity_result = Activity_Result.objects.create(solution=solution, is_correct=answer, patient=patient, is_completed=True)
        activity_result.save()
        
        return render(request, "patient_home.html")


    
    context = { 'load': True, 'solution': solution, 'training': False, 'prueba': json_c }

    return render(request,  path_activity+ '/' +  activity.name + '.html', context)



  