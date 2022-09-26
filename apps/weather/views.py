from rest_framework import viewsets
from apps.weather.models import WeatherType
from apps.weather.serializers import WeatherTypeSerializers
from rest_framework.response import Response
from django.http import Http404


# Create your views here.

class WeatherTypeViewSet(viewsets.ModelViewSet):
    queryset = WeatherType.objects.all()
    serializer_class = WeatherTypeSerializers

    def get_queryset(self):
        print(self.request.user.is_staff)
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            raise Http404
            # queryset=WeatherType.objects.none()
            # return Response({'detail':'You do not have the permissions to get the data'})