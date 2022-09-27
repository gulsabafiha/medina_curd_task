from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.weather.models import WeatherType
from apps.weather.permissions import IsStaff
from apps.weather.serializers import WeatherTypeSerializers
from django.http import Http404


# Create your views here.

class WeatherTypeViewSet(viewsets.ModelViewSet):
    queryset = WeatherType.objects.all()
    serializer_class = WeatherTypeSerializers
    permission_classes = [IsStaff, ]
    authentication_classes = [JWTAuthentication]