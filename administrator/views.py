from django.shortcuts import redirect, render
from principal.models import User, Doctor, Patient
from .forms import CreateDoctorForm, CreatePatientForm
from principal.utils import get_user_by_token


# Create your views here.

def admin_home(request):
    user = User.objects.get(username=get_user_by_token(request))
    context = {'admin': user}
    return render(request, "admin_home.html", context)

def form_doctor(request):

    if request.method == 'POST':
        doctor_form = CreateDoctorForm(request.POST,"form")
        if doctor_form.is_valid():
            username = doctor_form.cleaned_data['username']
            password = doctor_form.cleaned_data['password']
            first_name = doctor_form.cleaned_data['first_name']
            last_name = doctor_form.cleaned_data['last_name']
            birth_date = doctor_form.cleaned_data['birth_date']
            comments = doctor_form.cleaned_data['comments']
            specialty = doctor_form.cleaned_data['specialty']
            email = doctor_form.cleaned_data['email']

            
            user = User.objects.create(username=username, password=password , first_name=first_name, last_name=last_name, birth_date=birth_date, comments=comments, is_medic=True, email=email)
            user.set_password(password)
            user.save()

            doctor = Doctor.objects.create(user=user ,specialty=specialty)
            doctor.save()

            return redirect(to=all_doctors)

    else:
        doctor_form  = CreateDoctorForm()

    context = {'form': doctor_form}

    return render(request, 'create_doctor.html', context)

def form_patient(request):
    if request.method == 'POST':
        patient_form = CreatePatientForm(request.POST,"form")
        if patient_form.is_valid():
            username = patient_form.cleaned_data['username']
            password = patient_form.cleaned_data['password']
            first_name = patient_form.cleaned_data['first_name']
            last_name = patient_form.cleaned_data['last_name']
            birth_date = patient_form.cleaned_data['birth_date']
            comments = patient_form.cleaned_data['comments']
            sickness = patient_form.cleaned_data['sickness']
            email = patient_form.cleaned_data['email']
            
            user = User.objects.create(username=username, password=password , first_name=first_name, last_name=last_name, birth_date=birth_date, comments=comments, is_patient=True, email=email)
            user.set_password(password)
            user.save()

            patient = Patient.objects.create(user=user ,sickness=sickness)
            patient.save()
            
            return redirect(to=all_patients)
    else:
        patient_form = CreatePatientForm()


    context = {'form':patient_form}

    return render(request, 'create_patient.html', context)

def user_types(request):
    return render(request, 'user_types.html')

def all_patients(request):
    patients = Patient.objects.all()

    context = {'patients': patients}

    return render(request, 'all_patients.html', context)


def all_doctors(request):
    doctors = Doctor.objects.all()

    context = {'doctors': doctors}

    return render(request, 'all_doctors.html', context)

def delete_user(request):
    try:
        
      is_doctor = True  
      user = User.objects.get(pk=request.GET['user'])

      if(user.is_patient):
          is_doctor = False

      user.delete()

      if(is_doctor):
          return redirect(to=all_doctors)
      else:
          return redirect(to=all_patients)


    except:
        return redirect(to=admin_home)

def update_patient(request):
    pass

def update_doctor(request):
    pass
