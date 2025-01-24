from django import forms
from .models import Patient

class Information(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'gender', 'number']  # imported from the Patient model