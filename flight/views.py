from django.shortcuts import render

# Create your views here.
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, ReservationSerializer, PassengerSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class FlightViewSet(viewsets.ModelViewSet):
  queryset = Flight.objects.all()
  serializer_class = FlightSerializer
  permissions_class = [IsAuthenticated]
  authentication_classes = (TokenAuthentication,)
  
  
class ReservationViewSet(viewsets.ModelViewSet):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer
  permissions_class = [IsAuthenticated]
  authentication_classes = (TokenAuthentication,)
 

class PassengerViewSet(viewsets.ModelViewSet):
  queryset = Passenger.objects.all()
  serializer_class = PassengerSerializer
  permissions_class = [IsAuthenticated]
  authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  



