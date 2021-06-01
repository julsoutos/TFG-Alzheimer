
from .views import patient_home
from django.shortcuts import render, redirect
import datetime
from principal.models import Patient_training, Test_Result, User, Patient
from principal.utils import get_user_by_token
from .utils import birth

path_activity = 'activities/'

def mental_test(request):

    user = User.objects.get(username=get_user_by_token(request))
    patient = Patient.objects.get(user=user)
    patient_training = Patient_training.objects.get(pk=request.GET['patient_training'], is_completed=False, patient=patient)

    tests = Test_Result.objects.filter(patient_training=patient_training, is_completed=False)

    if tests.count() < 1:
        patient_training = Patient_training.objects.get(pk=request.GET['patient_training'])
        patient_training.is_completed = True
        patient_training.end_date = datetime.date.today()
        patient_training.save()

        return render(request, "end_training.html")

    context = {"page": path_activity + tests[0].mental_Test.name + ".html", "patient_training": request.GET['patient_training'], "test_pk": tests[0].pk}

    return render(request, "init_mental.html", context)

def load_mental_test(request):

    if request.method == "POST":
        patient_training = Patient_training.objects.get(pk=request.POST['patient_training'])
        test_mental = Test_Result.objects.get(pk=request.POST['test_mental'])
        test_mental.is_completed = True
        test_mental.puntuation = evaluate_test(request, test_mental)
        test_mental.save()

        context = {"patient_training": patient_training}

        return render(request, "mental_test.html", context)

def evaluate_test(request, test):
    
    if(test.mental_Test.name == 'Isaac Test'):
        animal = request.POST['answer1']
        color = request.POST['answer2']
        fruit = request.POST['answer3']
        
       

        return int(animal) if animal != "" else 0 + int(color) if color != "" else 0 + int(fruit) if fruit != "" else 0 

    if(test.mental_Test.name == 'Hodkinson Test'):
        count = 0
        user = User.objects.get(username=get_user_by_token(request))
        patient = Patient.objects.get(user=user)
        age = request.POST['answer1']
        year = request.POST['answer2']
        city = request.POST['answer3']
        birth_year = request.POST['answer4']
        adress = request.POST['answer5']
        king = request.POST['answer6']
        numbers = request.POST['answer7']

        if(int(age) == birth(user.birth_date)):
            print("1")
            count = count + 1

        date = datetime.date.today()
        if( int(year) == date.year):
            print("2")
            count = count + 1

        if(city == patient.city):
            print("3")
            count = count + 1

        print(user.birth_date.year)
        if(int(birth_year) == user.birth_date.year):
            print("4")

            count = count + 1

        if(adress == patient.address):
            print("5")

            count = count + 1

        if(king == "Felipe"):
            print("6")

            count = count + 1
        
        if(numbers == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"):
            print("7")

            count = count + 1
        return count
