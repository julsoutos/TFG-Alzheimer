from principal.models import User
from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )

    def clean_password(self):
        data1 = self.cleaned_data['username'].strip()
        data2 = self.cleaned_data['password'].strip()
      
        auth = authenticate(username=data1, password=data2)

        if auth is None:
            raise forms.ValidationError('El usuario o contraseña es incorrecto', "password")
        return data2


 