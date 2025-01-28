from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import Information
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
#serialzer code

#this patient_list helps to get all the list of patient admitted in hospital
@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many = True)
    return Response(serializer.data)
@api_view(['GET','POST'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk = pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data) 
    except Patient.DoesNotExist:
        return Response({'error': 'Patient doesnt not exist'}, status = 404)

@api_view(['POST'])
def patient_create(request):  # To create a patient if anyone arrives
    serializer = PatientSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['PUT'])
def patient_update(request, pk):  # To update the patient
   patient = Patient.objects.get(id = pk)
   serializer = PatientSerializer(instance = patient, data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
   return Response(serializer.errors)


@api_view(['DELETE'])
def patient_delete(request, pk):  # To delete the patient
    patient = Patient.objects.get(id = pk)
    patient.delete()
    return Response({"message": "patient deleted successfully"})

# Dashboard view
def dashboard_view(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/dashboard.html',
                  {'patients': patients,}) # Render the dashboard template
    
def patient_form(request):
    return render(request, 'hospital/patient_form.html')

def patient_delete(request):
    return render(request, 'hospital/patient_confirm_delete.html')
