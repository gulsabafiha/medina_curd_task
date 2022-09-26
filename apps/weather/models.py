from django.db import models


# Create your models here.

class WeatherType(models.Model):
    name = models.CharField(max_length=100)
    high_value = models.FloatField(verbose_name='Temperature High Value')
    low_value = models.FloatField(verbose_name='Temperature Low Value')

    def __str__(self):
        return self.name

