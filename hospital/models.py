from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES= [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('U', 'Undisclosed'), #If user doesnt select gender it will be selected as undisclosed
    ]
    STATUS = [
        ('Ongoing', 'Ongoing'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length = 1,  choices = GENDER_CHOICES, default='U')
    number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS, default = "Pending")
    
    def __str__(self): #it converts object to string
        return self.name
    
class Doctor(models.Model):
    # doctor_id = models.IntegerField()
    name = models.CharField(max_length=50)
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Bed(models.Model):
    bed_num = models.IntegerField()
    patient_name = models.ForeignKey(Patient, on_delete= models.CASCADE)
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Bed {self.bed_num}" #returns the bed number in string format
    
class Treatments(models.Model):
    STATUS = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)  # Use `choices` here

    def __str__(self):
        return f"Treatment for {self.patient} by doctor {self.doctor}"
    
    
    
    
    