from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from principal.models import User
from datetime import date
import re
from django.core.exceptions import ValidationError
from django import forms
import logging


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
        widget=forms.EmailInput(attrs={'class': "form-control"}),
        required=True, max_length=100
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"}),
        required=True, max_length=1000
    )

    # def clean_birth_date(self):
    #         birth_date = self.cleaned_data['birth_date']
    #         print('fecha')
    #         if birth_date>=date.today() :
                
    #             raise ValidationError('birth_date', "La fecha de nacimiento no puede ser posterior a la actual")
    #         return birth_date
    
    # def clean_email(self):
    #         email = self.cleaned_data['email']
    #         expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    #         print('re.match(expresion_regular, email)')
    #         if re.match(expresion_regular, email) is None:
    #             print('correo')
    #             raise ValidationError('email', "El formato del email no es correcto")
    #         return email

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
        widget=forms.EmailInput(attrs={'class': "form-control"}),
        required=True, max_length=100
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"}),
        required=True, max_length=1000
    )
      
