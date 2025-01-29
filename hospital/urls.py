from django.contrib import admin
from django.urls import path
from .views import *
from . import views
from .views import *

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),  # Ensure this view lists patients
     path('patients/create/', PatientCreateAPIView.as_view(), name='patient_create'),  # For POST (Create)
    path('patients/<int:pk>/', PatientDetailAPIView.as_view(), name='patient_detail'),
    path('patients/update/<int:pk>/', PatientDetailAPIView.as_view(), name='patient_update'),  # For PUT (Update)
    path('patients/delete/<int:pk>/', PatientDetailAPIView.as_view(), name='patient_delete'),  # For DELETE (Delete)

    path('dashboard/', dashboard_view, name='dashboard')  # Ensure this view is implemented
]
