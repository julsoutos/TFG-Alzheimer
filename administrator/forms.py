from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from principal.models import Doctor, Patient, User
import datetime
from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'

class CreateDoctorForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    specialty = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )

    birth_date = forms.DateField(
        widget= DateInput(attrs={'class': "form-control"}),
        required=True
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "example@gmail.com"}),
        required=True, max_length=100
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"}),
         max_length=400, required=False
    )

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']

        if data>=datetime.date.today():
            raise forms.ValidationError('La fecha de nacimiento no puede ser igual o posterior a la actual', "birth_date")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']

        if len(data) < 6:
            raise forms.ValidationError('Debe tener un mínimo de 6 carácteres', "password")
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        users = User.objects.filter(username=data)

        if(users.count() > 0):
            raise forms.ValidationError('El nombre de usuario no está disponible', "username")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        users = User.objects.filter(email=data)

        if(users.count() > 0):
            raise forms.ValidationError('Este correo ya ha sido registrado en la aplicación', "email")
        return data

class CreatePatientForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    sickness = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=300
    )
    birth_date = forms.DateField(
        widget= DateInput(attrs={'class': "form-control"}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "example@gmail.com"}),
        required=True, max_length=100
    )
    
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=200
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=200
    )

    doctor = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=200
    )

    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"}),
        max_length=400, required=False
    )
      
    def clean_birth_date(self):
            data = self.cleaned_data['birth_date']
 
            if data>=datetime.date.today():
                raise forms.ValidationError('La fecha de nacimiento no puede ser igual o posterior a la actual', "birth_date")
            return data
             
    def clean_password(self):
        data = self.cleaned_data['password']

        if len(data) < 6:
            raise forms.ValidationError('Debe tener un mínimo de 6 carácteres', "password")
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        users = User.objects.filter(username=data)

        if(users.count() > 0):
            raise forms.ValidationError('El nombre de usuario no está disponible', "username")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        users = User.objects.filter(email=data)

        if(users.count() > 0):
            raise forms.ValidationError('Este correo ya ha sido registrado en la aplicación', "email")
        return data

class UpdatePatientForm(forms.Form):
    username = forms.CharField(
    widget=forms.TextInput(attrs={'class': "form-control"}),
    required=True, max_length=50
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    
    birth_date = forms.DateField(
        widget= DateInput(attrs={'class': "form-control"}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "example@gmail.com"}),
        required=True, max_length=100
    )
    
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"}),
        max_length=400, required=False
    )
    sickness = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=300
    )
         
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=200
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=200
    )
    doctor = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=200
    )

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(UpdatePatientForm, self).__init__(*args, **kwargs)

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        if data>=datetime.date.today():
            raise forms.ValidationError('La fecha de nacimiento no puede ser igual o posterior a la actual', "birth_date")
        return data

    def clean_username(self):
        try:
            data = self.cleaned_data['username']
            user = Patient.objects.get(user__username=data)
            if(self.pk != user.pk):
                raise forms.ValidationError('El nombre de usuario no está disponible', "username")
            return data
        except:
            return data
    def clean_email(self):
        try:
            data = self.cleaned_data['email']
            user = Patient.objects.get(user__email=data)
            if(self.pk != user.pk):
                raise forms.ValidationError('Este correo ya ha sido registrado en la aplicación', "email")
            return data
        except:
            return data


class UpdateDoctorForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    specialty = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    birth_date = forms.DateField(
        widget= DateInput(attrs={'class': "form-control"}),
        required=True
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "example@gmail.com"}),
        required=True, max_length=100
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"}),
         max_length=400, required=False
    )

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super(UpdateDoctorForm, self).__init__(*args, **kwargs)

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        if data>=datetime.date.today():
            raise forms.ValidationError('La fecha de nacimiento no puede ser igual o posterior a la actual', "birth_date")
        return data

    def clean_username(self):
        try:
            data = self.cleaned_data['username']
            user = Doctor.objects.get(user__username=data)
            if(self.pk != user.pk):
                raise forms.ValidationError('El nombre de usuario no está disponible', "username")
            return data
        except:
            return data

    def clean_email(self):
        try:
            data = self.cleaned_data['email']
            user = Doctor.objects.get(user__email=data)
            if(self.pk != user.pk):
                raise forms.ValidationError('Este correo ya ha sido registrado en la aplicación', "email")
            return data
        except:
            return data 

class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )

        
    def clean_password1(self):
        data = self.data['password1']

        if len(data) < 6:
            raise forms.ValidationError('Debe tener un mínimo de 6 carácteres', "password1")
            
        return data


    def clean_password2(self):
        res = ""
        data1 = self.data['password1']
        data2 = self.data['password2']

        if(data1 != data2):
            res = res + "Las contraseñas son diferentes."


        if len(data2) < 6:
            res = res +  'Debe tener un mínimo de 6 carácteres'

        if res != "":
            raise forms.ValidationError(res, "password2")

        return data2
