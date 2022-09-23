from django.db import models


class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)


class VendorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(groups__name='vendor')

class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(groups__name='customer')
