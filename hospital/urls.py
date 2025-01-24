from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('patients/', patient_list, name = 'patient_list'),
    path('patients/<int:pk>', patient_detail, name = 'patient_detail'),
    path('patients/<int:pk>', patient_create, name = 'patient_create'),
    path('patients/<int:pk>', patient_update, name = 'patient_update'),
    path('patients/<int:pk>', patient_delete, name = 'patient_delete'),
    
<<<<<<< HEAD
    #new url path
    path('dashboard/', dashboard_view, name = 'dashboard')
=======
>>>>>>> b7c799f11c8bbc13508e7c543222b90aebdce612
]
