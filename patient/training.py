from principal.models import Activity_Training, Activity, Solution, User, Patient_training, Patient
from django.shortcuts import render, redirect
from .utils import get_solution, evaluate
from principal.utils import get_user_by_token
from datetime import date

path_activity = 'activities/'


def list_trainings(request):

    user = User.objects.get(username=get_user_by_token(request))
    patient = Patient.objects.get(user=user)
    trainings = Patient_training.objects.filter(patient=patient, is_completed=False)

    if request.GET:

        patient_training = Patient_training.objects.get(pk=request.GET['training'], is_completed=False, patient=patient)

        context = {'training': patient_training, 'start': True}
        
        return render(request, "trainings.html", context)


    context = {'trainings': trainings}

    return render(request, "trainings.html", context)




def init_training(request):

    user = User.objects.get(username=get_user_by_token(request))
    patient = Patient.objects.get(user=user)
    patient_training = Patient_training.objects.get(pk=request.GET['training'], is_completed=False, patient=patient)

    activities = Activity_Training.objects.filter(patient_training=patient_training, is_completed=False)
    

    if not activities:

        context = {"patient_training": patient_training, "load": True}
        
        return render(request, "mental_test.html", context)


    context = { 'page': path_activity + activities[0].activity.name + '.html', 'activity': activities[0].activity, 'solution': get_solution(request, activities[0].activity), 'training': True, 'load': False, 'pk':  patient_training.pk  }

    return render(request, path_activity + 'training.html', context)

   


def load_training(request):

    user = User.objects.get(username=get_user_by_token(request))
    patient = Patient.objects.get(user=user)
    patient_training = Patient_training.objects.get(pk=request.GET['training'], is_completed=False, patient=patient)
    activities = Activity_Training.objects.filter(patient_training=patient_training, is_completed=False)

    if request.method == 'POST':

        a = Activity_Training.objects.get(pk = request.POST['activity'])
        a.is_completed = True
        solution = Solution.objects.get(name = request.GET['activity'])
        answer = evaluate(request, solution, 'answer')
        a.is_correct = answer
        a.save()

    
        all_activities = Activity_Training.objects.filter(patient_training=patient_training)

        context = {'training': patient_training.pk, 'num_activities': all_activities.count(), 'next': True, 'activities': all_activities.count() - activities.count()}

        return render(request, path_activity + 'training.html', context)    

    else:
    
        activity = Activity.objects.get(name = request.GET['name'])
        solution = Solution.objects.get(name = request.GET['activity'])
        
        
        context = { 'page': path_activity + activity.name + '.html', 'activity': activity, 'solution': solution, 'activity_training':  activities[0] ,  'training': True, 'load': True }

    
        return render(request, path_activity + 'training.html', context)



    