
from django.shortcuts import render, redirect
import datetime
from principal.models import Patient_training

def mental_test(request):

    load = False
    context = {"load": load}

    return render(request, "mental_test.html", context)

def load_mental_test(request):

    if request.method == "POST":
        patient_training = Patient_training.objects.get(pk=request.GET['patient_training'])
        patient_training.is_completed = True
        patient_training.end_date = datetime.date.today()
        patient_training.save()

        return redirect(to="patient_home")
    
    else:
        load = True
        context = {"load": load}

        return render(request, "mental_test.html", context)

def evaluate_test():
    pass