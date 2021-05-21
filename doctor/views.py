
from django.shortcuts import redirect, render
from principal.models import  User, Doctor, Patient, Training, Activity
from principal.utils import  get_user_by_token
from patient.utils import birth
# Create your views here.

def doctor_home(request):

    user = User.objects.get(username=get_user_by_token(request))

    context = {'doctor': user}

    return render(request, 'doctor_home.html', context)

def patients(request):

    try:
        user = User.objects.get(username=get_user_by_token(request))

        context = {'patients': get_patients(request), 'age': birth(user.birth_date) }

        return render(request, 'patients.html', context)

    except:
        return redirect(to="doctor_home")


def trainings(request):

    user = User.objects.get(username=get_user_by_token(request))
    doctor = Doctor.objects.get(user=user)

    trainings = Training.objects.filter(doctor=doctor)


    context = {'trainings': trainings}

    return render(request, "list_trainings.html", context)


def training_details(request):

    return render(request, "training_details.html")

def create_training(request):
    
    try:
        user = User.objects.get(username=get_user_by_token(request))

        context = {'patients': get_patients(request),  'age': birth(user.birth_date), 'activities': get_all_activities() }

        return render(request, "create_training.html", context)

    except:
        return redirect(to="doctor_home")


def get_patients(request):

    user = User.objects.get(username=get_user_by_token(request))
    doctor = Doctor.objects.get(user=user)
    patients = Patient.objects.filter(doctor=doctor)

    return patients

def get_all_activities():

    return Activity.objects.all()

    
