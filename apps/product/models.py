from django.db import models
from apps.weather.models import WeatherType

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    weather_type = models.ForeignKey(WeatherType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
