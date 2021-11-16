# Django--React-Flight-python -m venv venv
source ./venv/Scripts/activate
pip install Django
pip install djangorestframework
pip install python-decouple
django-admin startproject Project .
python manage.py startapp FlightApi

pip install django-phonenumber-field
INTALL APP
'phonenumber_field',
pip install phonenumbers

from phonenumber_field.modelfields import PhoneNumberField


takvim den seçim yapmak için

from django.utils import timezone


POSTMAN de http://localhost:8000/logout/  LOGOUT yapabilmek için headers bölümüne Authenticate Token ekle


API bağlantısı için CORS

1-pip install django-cors-headers
2-INSTALLED APPLI
 'corsheaders',

3-MIDDLEWARE 
  CommonMidelware in üstünde olacak şekilde kopyala
  'corsheaders.middleware.CorsMiddleware',

4- settings.py 
 yapıştır
 CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
]