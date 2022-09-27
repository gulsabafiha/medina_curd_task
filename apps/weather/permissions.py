from rest_framework import permissions


class Iscustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='customer'):
            return True
        return False


class Isvendor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='vendor'):
            return True
        return False