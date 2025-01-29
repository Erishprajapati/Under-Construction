from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import Information
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PatientSerializer
from rest_framework import status
from rest_framework.serializers import ValidationError

# Create your views here.
#serialzer code

#this patient_list helps to get all the list of patient admitted in hospital
@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many = True)
    return Response(serializer.data)
# @api_view(['GET','POST'])
# def patient_detail(request, pk):
#     try:
#         patient = Patient.objects.get(pk = pk)
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data) 
#     except Patient.DoesNotExist:
#         return Response({'error': 'Patient doesnt not exist'}, status = 404)

# @api_view(['POST'])
# def patient_create(request):  # To create a patient if anyone arrives
#     serializer = PatientSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
    
# @api_view(['GET','PATCH','PUT'])
# def patient_update(request, pk):  # To update the patient
#     try:
#         patient = Patient.objects.get(pk = pk) #first get the data of the user that you want to update
#     except Patient.DoesNotExist:
#         return Response({'error': 'patient not found'}, status = 404)
#     if request.method == 'GET':
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)
#     elif request.method in ['PUT', 'PATCH']:
#         serializer = PatientSerializer(patient,data=request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = 404)
    

# @api_view(['DELETE'])
# def patient_delete(request,pk):  # To delete the patient
#     patient = Patient.objects.get(id = pk)
#     patient.delete()
#     return Response({"Message": "Patient deleted"})
    
#writing the class based views 
class PatientDetailAPIView(APIView):
    def get(self,request, pk):
        patient = get_object_or_404(Patient, pk = pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self,request, pk):
        patient = get_object_or_404(Patient, pk = pk)
        serializer = PatientSerializer(patient, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Details":"Patient updated successfully" })
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        patient = get_object_or_404(Patient, pk = pk)
        patients = Patient.objects.filter(Patient__treatment = patient).count()
        if patients > 0:
            raise ValidationError({"Details" :  "Treatment is still left for this patient."})
        patient.delete()
        return Response({"Description": "Patient Information deleted successfully."})
 
class PatientCreateAPIView(APIView):
    def post(self,request):
        serializer = PatientSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"Description": "Patient created and saved data into database."})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Dashboard view
def dashboard_view(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/dashboard.html',
                  {'patients': patients,}) # Render the dashboard template
    
def patient_form(request):
    return render(request, 'hospital/patient_form.html')

def patient_delete(request):
    return render(request, 'hospital/patient_confirm_delete.html')
