from django import forms
from .models import UserProfile

class NumDepartamentoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['num_departamento']
        widgets = {
            'num_departamento': forms.TextInput(attrs={'placeholder': 'Ingresa tu número de departamento', 'class': 'form-control'})
        }
