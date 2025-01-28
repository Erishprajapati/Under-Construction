# from rest_framework import serializers
# from .models import *

# class PatientSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     gender = serializers.CharField(max_length = 1,  choices = Patient.GENDER_CHOICES, default='U')
#     number = serializers.CharField(max_length=10)
#     status = serializers.CharField(max_length=20, choices= Patient.STATUS, default = "Pending")
    
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=Patient.GENDER_CHOICES, default='U')  # Use ChoiceField for choices
    status = serializers.ChoiceField(choices=Patient.STATUS, default="Pending")   # Use ChoiceField here too
