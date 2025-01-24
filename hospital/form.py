from django import forms 
from .models import Patient

class Information(forms.Model):
    model = Patient
    fields = ['name', 'gender', 'number'] #imported from patient in model function