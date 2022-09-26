from rest_framework import permissions
# from django.contrib.auth import Group

class Iscustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='customers'):
            return True
        return False


class Isvendor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='vendor'):
            return True
        return False