from django.contrib import admin
#import the admin module and classes
from .models import *

# Register your models here.


# @admin.register(Patient)
# class Patient(admin.ModelAdmin):
#     list_display = ['id','name', 'gender', 'number']
#     list_editable = ['name',]
#     readonly_fields = ('gender', 'number')
    
    
# @admin.register(Doctor)
# class Doctor(admin.ModelAdmin):
#     list_display = ['id','name', 'is_available']
#     readonly_fields = ['id', 'name']
#     list_editable = ['is_available']
    
# @admin.register(Bed)
# class Bed(admin.ModelAdmin):
#     list_display=['bed_num','patient_name','is_available']
    
# @admin.register(Treatments)
# class Treatments(admin.ModelAdmin):
#     list_display = ['patient','doctor', 'status']
#     list_editable = ['doctor','status']


class BedInline(admin.TabularInline):
    model = Bed
    extra = 1
class TreatmentInline(admin.TabularInline):
    model = Treatments
    extra = 1

@admin.register(Patient)
class Patient(admin.ModelAdmin):
    list_display = ['id','name','gender','number', 'status']
    inlines = [BedInline, TreatmentInline]

@admin.register(Bed)
class Bed(admin.ModelAdmin):
    list_display=['bed_num','patient_name','is_available']
    
@admin.register(Treatments)
class Treatments(admin.ModelAdmin):
    list_display = ['patient','doctor', 'status']
    list_editable = ['doctor','status']
    
@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ['name', 'is_available']
    list_editable = ['is_available']