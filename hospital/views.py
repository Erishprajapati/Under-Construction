from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import Information

# Create your views here.
def patient_list(request):
    patients = Patient.objects.all()  #this shows the name of all the patients
    return render(request, 'patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_detail.html', {'patient': patient})

def patient_create(request): #to create the patient if anyone arrives
    if request.method == 'POST': #using the post method 
        form = Information(request.POST) #if post method is used it sends data to server
        if form.is_valid(): #if form contains the name number and gender then form is valid
            form.save()#form valid == form.save()
            return redirect('patient_list')
        else:
            form = Information()
            return render(request, 'patient_form.html', {'form': form})
            

def patient_update(request,pk): #to update the patient
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = Information(request.POST, instance = patient)
        if form.is_valid():
            form.save()#form valid == form.
        else:
            form = Information(instance = patient)
            return render(request, 'patient_form.html', {'form': form})
        
def patient_delete(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_confirm_delete.html', {'patient': patient})

def dashboard_view(request):
    return render(request, 'hospital/dashboard.html')