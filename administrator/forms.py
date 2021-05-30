from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from principal.models import User
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
         max_length=1000
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
        required=True, max_length=1000
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
        max_length=1000
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