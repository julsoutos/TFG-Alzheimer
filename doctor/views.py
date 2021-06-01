
from patient.mental_test import mental_test
from django.shortcuts import redirect, render, resolve_url
from principal.models import  Mental_Test, Patient_training, Test_Result, User, Doctor, Patient, Training, Activity, Activity_Training
from principal.utils import  get_user_by_token
from patient.utils import birth
from .forms import CreateTrainingForm
# Create your views here.

def doctor_home(request):

    user = User.objects.get(username=get_user_by_token(request))

    context = {'doctor': user}

    return render(request, 'doctor_home.html', context)

def patients(request):

    try:
        user = User.objects.get(username=get_user_by_token(request))

        context = {'patients': get_patients(request) }

        return render(request, 'patients.html', context)

    except:
        return redirect(to="doctor_home")

def patient_details(request):

    patient = Patient.objects.get(pk=request.GET['patient'])

    context = {'patient': patient}

    return render(request, 'patient_details.html',context)


def trainings(request):

    user = User.objects.get(username=get_user_by_token(request))
    doctor = Doctor.objects.get(user=user)

    trainings = Training.objects.filter(doctor=doctor)


    context = {'trainings': trainings}

    return render(request, "list_trainings.html", context)


def training_details(request):

    training = Training.objects.get(pk=request.GET['training'])

    patients = Patient_training.objects.filter(training=training)

    activities = Activity_Training.objects.filter(patient_training__training = training)

    context = {'training': training, 'activities': activities, 'patients': patients}

    return render(request, "training_details.html", context)



def delete_training(request):

    try:
        training = Training.objects.get(pk=request.GET['training'])
        training.delete()
        return redirect(to=trainings)

    except:
        return redirect(to=trainings)
    



def create_training(request):
    
 
    user = User.objects.get(username=get_user_by_token(request))

    if request.method == 'POST':
        create_training_form = CreateTrainingForm(request.POST, "form")
        if create_training_form.is_valid():
            name = create_training_form.cleaned_data['name']
            description = create_training_form.cleaned_data['description']
            doctor = Doctor.objects.get(user=user)
            training = Training.objects.create(name=name, description=description, doctor=doctor)
            training.save()

            create_activity_trainings(request, training, create_training_form)

            return redirect(to=trainings)
    else:
        create_training_form = CreateTrainingForm()

    context = {'patients': get_patients(request),  'activities': get_all_activities(), "form": create_training_form, 'tests': Mental_Test.objects.all() }

    return render(request, "create_training.html", context)


def get_patients(request):

    user = User.objects.get(username=get_user_by_token(request))
    doctor = Doctor.objects.get(user=user)
    patients = Patient.objects.filter(doctor=doctor)

    return patients


def get_all_activities():

    return Activity.objects.all()


def create_activity_trainings(request, training, create_training_form):
    patients =  create_training_form.cleaned_data['inputPatients'].split(",")
    activities = create_training_form.cleaned_data['inputActivities'].split(",")
    tests = create_training_form.cleaned_data['inputTests'].split(",")
   
    for username in patients:
        
        user = User.objects.get(username=username)
        patient = Patient.objects.get(user=user)
        patient_training = Patient_training.objects.create(training=training, patient=patient, is_completed=False)
        patient_training.save()
        
        for name in activities:
            
            activity = Activity.objects.get(name=name)
            
            activity_training = Activity_Training.objects.create(name="", activity=activity, patient_training=patient_training, is_completed=False, is_correct=False)
            activity_training.save()

        for test in tests:
            mental_test = Mental_Test.objects.get(name=test)
            
            mental_result = Test_Result.objects.create(patient_training=patient_training, mental_Test=mental_test, is_completed=False)
            mental_result.save()




def activities(request):

    context = {"activities": get_all_activities()}

    return render(request, "list_activities.html", context)

def activity_details(request):

    try:
        activity = Activity.objects.get(pk=request.GET["activity"])

        context = {"activity": activity}

        return render(request, "activity_details.html", context)

    except:
        return redirect(to=doctor_home)


def trainings_completed(request):

    try:
        patient = Patient.objects.get(pk=request.GET['patient'])
        patient_trainings = Patient_training.objects.filter(patient=patient, is_completed=True)

        context = {"trainings": patient_trainings}

        return render(request, "trainings_completed.html", context)


    except:
        return redirect(to=doctor_home)

def tests(request):

    context = {"tests": Mental_Test.objects.all()}

    return render(request, "list_test.html", context)