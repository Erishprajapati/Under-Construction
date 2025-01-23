from django.contrib import admin
#import the admin module and classes
from .models import Patient, Doctor, Bed, Treatments

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Bed)
admin.site.register( Treatments)

