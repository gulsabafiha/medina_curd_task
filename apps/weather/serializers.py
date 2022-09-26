from rest_framework import serializers

from apps.weather.models import WeatherType


class WeatherTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeatherType
        fields = ['name', 'high_value', 'low_value']
