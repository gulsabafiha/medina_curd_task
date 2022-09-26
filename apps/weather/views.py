from rest_framework import viewsets
from apps.weather.models import WeatherType
from apps.weather.serializers import WeatherTypeSerializers


# Create your views here.

class WeatherTypeViewSet(viewsets.ModelViewSet):
    queryset = WeatherType.objects.all()
    serializer_class = WeatherTypeSerializers

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()