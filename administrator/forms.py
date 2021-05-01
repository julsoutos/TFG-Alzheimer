from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from principal.models import User
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateDoctorForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    specialty = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    birth_date = forms.DateField(
        widget= DateInput(attrs={'class': "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control"})
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"})
    )
    
class CreatePatientForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    sickness = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    birth_date = forms.DateField(
        widget= DateInput(attrs={'class': "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control"})
    )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"})
    )
      
