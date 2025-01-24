from django import forms 
from .models import Patient

class Information(forms.Model):
    model = Patient
<<<<<<< HEAD
    fields = ['name', 'gender', 'number'] #imported from patient in model function
=======
    fields = ['name', 'gender', 'number'] #imported from patient in model function
    
>>>>>>> b7c799f11c8bbc13508e7c543222b90aebdce612
