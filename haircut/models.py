from django.db import models

# Create your models here.
class Appointment(models.Model):
	time = models.CharField(max_length=180, null=True, blank=True)
	customer_name = models.CharField(max_length=180, null=True, blank=True)
	barber_name = models.CharField(max_length=180, null=True, blank=True)	