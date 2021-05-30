from django import forms



class CreateTrainingForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True, max_length=50
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control"}),
         max_length=1000, required=False
    )   
    inputPatients = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", "type": "hidden"}),
        max_length=1000, required=False
    )
    inputActivities = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", "type": "hidden"}),
        max_length=1000, required=False
    )

    def clean_inputActivities(self):
        
        data1 = self.cleaned_data['inputPatients']
        data2 = self.cleaned_data['inputActivities']
 
        if len(data1) < 1 or len(data2) < 1:
            raise forms.ValidationError("Debe añadir al menos un paciente y una actividad.", "inputActivities")
        return data2

  
 