from django.core.files.base import ContentFile
import administrator
from datetime import datetime
from django.shortcuts import redirect, render
from principal.models import Activity_Result, Patient_training, Training, User, Doctor, Patient
from .forms import CreateDoctorForm, CreatePatientForm, UpdateDoctorForm, UpdatePasswordForm, UpdatePatientForm
from principal.utils import get_user_by_token
from principal.views    import inicio


# Create your views here.

def admin_home(request):
    try:
        user = User.objects.get(username=get_user_by_token(request))
        context = {'admin': user, 'trainings': Patient_training.objects.filter(is_completed=True).count(), 
        'activities': Activity_Result.objects.filter(is_completed=True).count(), 'num_doctors': Doctor.objects.all().count(), 'num_patients': Patient.objects.all().count()}
        return render(request, "admin_home.html", context)
    except:
        return redirect(to=inicio)

def form_doctor(request):
    try:
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
    except:
        return redirect(to=all_doctors)

def form_patient(request):
    try:
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
                address = patient_form.cleaned_data['address']
                city = patient_form.cleaned_data['city']
                username_doctor = patient_form.cleaned_data['doctor']

                user = User.objects.create(username=username, password=password , first_name=first_name, last_name=last_name, birth_date=birth_date, comments=comments, is_patient=True, email=email)
                user.set_password(password)
                user.save()

                doctor = Doctor.objects.get(user__username = username_doctor.strip())

                patient = Patient.objects.create(user=user ,sickness=sickness, address=address, city=city, doctor=doctor)
                patient.save()
                
                return redirect(to=all_patients)
        else:
            patient_form = CreatePatientForm()


        context = {'form':patient_form}

        return render(request, 'create_patient.html', context)
    except:
        return redirect(to=all_patients)


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

    try:
        patient = Patient.objects.get(pk=request.GET['patient'])


        if request.method == "POST":
            form_user = UpdatePatientForm(request.POST, "form_user", pk=patient.pk)

            if form_user.is_valid():
                username = form_user.cleaned_data['username']
                first_name = form_user.cleaned_data['first_name']
                last_name = form_user.cleaned_data['last_name']
                birth_date = form_user.cleaned_data['birth_date']
                comments = form_user.cleaned_data['comments']
                sickness = form_user.cleaned_data['sickness']
                email = form_user.cleaned_data['email']
                address = form_user.cleaned_data['address']
                city = form_user.cleaned_data['city']
                username_doctor = form_user.cleaned_data['doctor']

                user = User.objects.get(pk=patient.user.pk)
                print(user)
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.birth_date = birth_date
                user.comments = comments
                user.email = email
                user.save()

                doctor = Doctor.objects.get(user__username = username_doctor.strip())

                edit_patient = Patient.objects.get(pk=patient.pk)
                edit_patient.sickness = sickness
                edit_patient.address = address
                edit_patient.city = city
                edit_patient.doctor = doctor
                edit_patient.save()
                
                return redirect(to=all_patients)
        else:
            form_user = UpdatePatientForm(initial={'username':patient.user.username, 'first_name': patient.user.first_name, 'last_name': patient.user.last_name,
            'email':patient.user.email, 'comments':patient.user.comments, 'birth_date':datetime.strftime( patient.user.birth_date, '%Y-%m-%d'),
            'address':patient.address, 'city': patient.city, 'sickness': patient.sickness, 'doctor':patient.doctor.user.username})

        context = {'form_user': form_user, 'user': patient.user.pk}

        return render(request, "update_patient.html", context)
    
    except:
        return redirect(to=all_patients)



def update_doctor(request):

    try:
        doctor = Doctor.objects.get(pk=request.GET['doctor'])


        if request.method == "POST":
            form_user = UpdateDoctorForm(request.POST, "form_user", pk=doctor.pk)

            if form_user.is_valid():
                username = form_user.cleaned_data['username']
                first_name = form_user.cleaned_data['first_name']
                last_name = form_user.cleaned_data['last_name']
                birth_date = form_user.cleaned_data['birth_date']
                comments = form_user.cleaned_data['comments']
                email = form_user.cleaned_data['email']
                specialty = form_user.cleaned_data['specialty']
        
                user = User.objects.get(pk=doctor.user.pk)
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.birth_date = birth_date
                user.comments = comments
                user.email = email
                user.save()

                edit_doctor = Doctor.objects.get(pk=doctor.pk)
                edit_doctor.specialty = specialty        
                edit_doctor.save()
                
                return redirect(to=all_doctors)
        else:
            form_user = UpdateDoctorForm(initial={'username':doctor.user.username, 'first_name': doctor.user.first_name, 'last_name': doctor.user.last_name,
            'email':doctor.user.email, 'comments':doctor.user.comments, 'birth_date':datetime.strftime( doctor.user.birth_date, '%Y-%m-%d'), 'specialty': doctor.specialty})

        context = {'form_user': form_user, 'user': doctor.user.pk}

        return render(request, "update_doctor.html", context)
    except:
        return redirect(to=all_doctors)

def update_password(request):

    user = User.objects.get(pk=request.GET['user'])
    if request.method == "POST":
        form = UpdatePasswordForm(request.POST or None, "form")
        if form.is_valid():
            password = form.cleaned_data['password1']   
            
            user.set_password(password)
            user.save()

            if user.is_patient:
                return redirect(to=all_patients)
            elif user.is_medic:
                return redirect(to=all_doctors)
            
    else:
        form = UpdatePasswordForm()
    context = {'form': form, 'user': user}

    return render(request, "update_password.html", context)


