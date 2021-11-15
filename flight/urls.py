from django.urls import path, include
from .views import FlightViewSet, ReservationViewSet, PassengerViewSet, UserViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('flight', FlightViewSet)
router.register('users', UserViewSet)
router.register('reservation', ReservationViewSet)
router.register('passenger', PassengerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]



# urlpatterns = [
#     path('flight/', FlightViewSet, name='flight'),
#     path('passenger/', PassengerViewSet, name='passenger'),
#     path('reservation/', ReservationViewSet, name='reservation'),
    
# ]






