
from django.shortcuts import redirect, render
from principal.models import  Patient_training, User, Doctor, Patient, Training, Activity, Activity_Training
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

        name = request.POST['name']
        description = request.POST['description']
        doctor = Doctor.objects.get(user=user)
        training = Training.objects.create(name=name, description=description, doctor=doctor)
        training.save()

        create_activity_trainings(request, training)

        return redirect(to=trainings)


    context = {'patients': get_patients(request),  'age': birth(user.birth_date), 'activities': get_all_activities() }

    return render(request, "create_training.html", context)


def get_patients(request):

    user = User.objects.get(username=get_user_by_token(request))
    doctor = Doctor.objects.get(user=user)
    patients = Patient.objects.filter(doctor=doctor)

    return patients


def get_all_activities():

    return Activity.objects.all()


def create_activity_trainings(request, training):

    patients = request.POST['inputPatients'].split(",")
    activities = request.POST['inputActivities'].split(",")

    for username in patients:
        
        user = User.objects.get(username=username)
        patient = Patient.objects.get(user=user)
        patient_training = Patient_training.objects.create(training=training, patient=patient, is_completed=False)
        patient_training.save()
        
        for name in activities:
            
            activity = Activity.objects.get(name=name)
            
            activity_training = Activity_Training.objects.create(name="", activity=activity, patient_training=patient_training, is_completed=False, is_correct=False)
            activity_training.save()

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

        

