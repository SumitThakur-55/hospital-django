from django.db import models

class Appointment(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)  # You can adjust the max_length based on your requirements
    date_of_appointment = models.DateField(null=True)
    doctor = models.CharField(max_length=100)