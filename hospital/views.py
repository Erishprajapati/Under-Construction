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
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many = True)
    return Response(serializer.data)
@api_view(['GET'])
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_detail.html', {'patient': patient})

def patient_create(request):  # To create a patient if anyone arrives
    if request.method == 'POST':  # Using the POST method
        form = Information(request.POST)  # If POST method is used, it sends data to server
        if form.is_valid():  # If form contains valid data (name, number, gender)
            form.save()  # Save the form data
            return redirect('patient_list')  # Redirect to the patient list page
    else:
        form = Information()  # If it's a GET request, just show an empty form
    return render(request, 'patient_form.html', {'form': form})

def patient_update(request, pk):  # To update the patient
    patient = get_object_or_404(Patient, pk=pk)  # Get the patient object or 404 if not found
    if request.method == 'POST':
        form = Information(request.POST, instance=patient)  # Prepopulate form with patient data
        if form.is_valid():
            form.save()  # Save the updated patient data
            return redirect('patient_list')  # Redirect to the patient list page
    else:
        form = Information(instance=patient)  # Prepopulate form with patient data for GET request
    return render(request, 'patient_form.html', {'form': form})

def patient_delete(request, pk):  # To delete the patient
    patient = get_object_or_404(Patient, pk=pk)  # Get the patient object or 404 if not found
    if request.method == 'POST':  # If POST request, delete the patient
        patient.delete()
        return redirect('patient_list')  # Redirect to the patient list page
    return render(request, 'patient_confirm_delete.html', {'patient': patient})  # Show confirmation page

# Dashboard view
def dashboard_view(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/dashboard.html',
                  {'patients': patients,}) # Render the dashboard template
    
def patient_form(request):
    return render(request, 'hospital/patient_form.html')

def patient_delete(request):
    return render(request, 'hospital/patient_confirm_delete.html')
