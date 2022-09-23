from django.db import models
from django.contrib.auth.models import Group
from apps.accounts.managers import AdminManager, CustomerManager, VendorManager
from django.contrib.auth.models import User


# Create your models here.
class Admin(User):
    class Meta:
        proxy = True

    objects = AdminManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        super(Admin, self).save(*args, **kwargs)


class Customer(User):
    class Meta:
        proxy = True

    objects = CustomerManager()

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='customer')
        self.groups.set([group])


class Vendor(User):
    class Meta:
        proxy = True

    objects = VendorManager()

    def save(self, *args, **kwargs):
        super(Vendor, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='vendor')
        self.groups.set([group])