# from rest_framework import serializers
# from .models import *

# class PatientSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     gender = serializers.CharField(max_length = 1,  choices = Patient.GENDER_CHOICES, default='U')
#     number = serializers.CharField(max_length=10)
#     status = serializers.CharField(max_length=20, choices= Patient.STATUS, default = "Pending")
    
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
    