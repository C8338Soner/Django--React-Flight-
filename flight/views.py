from django.shortcuts import render

# Create your views here.
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, ReservationSerializer, PassengerSerializer, UserSerializer, RegistrationSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

class FlightViewSet(viewsets.ModelViewSet):
  queryset = Flight.objects.all()
  serializer_class = FlightSerializer
  permission_classes = [IsAuthenticated]
  # authentication_classes = (TokenAuthentication,)
  
  
class ReservationViewSet(viewsets.ModelViewSet):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer
  permission_classes = [IsAuthenticated]
  # authentication_classes = (TokenAuthentication,)
 

class PassengerViewSet(viewsets.ModelViewSet):
  queryset = Passenger.objects.all()
  serializer_class = PassengerSerializer
  permission_classes = [IsAuthenticated]
  # authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            serializer.validated_data['password'] = make_password(password)
            user = serializer.save()
            # burdan sonra token olusturuyor. Aslinda buna gerek yok. zaten login oldugunda obtain_auth_token kullaniciya bir token veriyor. ama register oldugu anda token vermek istiyorsak asagidaki islemi yapiyoruz 
            token, _ = Token.objects.get_or_create(user=user) # varsa al yoksa olustur  ,_ bu bana gerekmedigi icin almiyorum
            data = serializer.data
            data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data)
            
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
          'message' : 'logout' 
        }
        return Response(data)
  



