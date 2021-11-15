from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Flight(models.Model):
 flightNumber = models.CharField(max_length=100)
 operatingAirlines = models.CharField(max_length=100)
 departureCity = models.CharField(max_length=100)
 dateOfDeparture = models.DateField(default = timezone.now)
 estimateTimeDeparture = models.PositiveIntegerField(null=True)
 def __str__(self):
  return self.flightNumber
 
 
class Passenger(models.Model):
 flight = models.ForeignKey(Flight, on_delete = models.CASCADE, null=True)
 firstName = models.CharField(max_length=100)
 lastName = models.CharField(max_length=100)
 email = models.EmailField(max_length=254)
 phone = PhoneNumberField()
 updateDate = models.DateField(auto_now=True)
 createdDate = models.DateField(auto_now_add=True)
 
 def __str__(self):
  return self.firstName
  
  
class Reservation(models.Model):
 flight = models.ForeignKey(Flight, on_delete = models.CASCADE, null =True)
 passenger = models.ForeignKey(Passenger, on_delete = models.CASCADE, null =True)
 user = models.ForeignKey(User, on_delete = models.CASCADE, null =True)
  
 def __str__(self):
  return str(self.passenger)