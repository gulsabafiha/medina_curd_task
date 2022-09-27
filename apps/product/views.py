from rest_framework import viewsets
from apps.product.models import Product, ProductType
from apps.product.serializers import ProductSerializers, ProductTypeSerializers
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from django.http import Http404

from apps.weather.permissions import Isvendor, Iscustomer


# Create your views here.

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializers

    def get_queryset(self):
        print(self.request.user.is_staff)
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            raise Http404


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         self.permission_classes = [Isvendor, ]
    #         print(self.permission_classes)
    #     return super(ProductViewSet, self).get_permissions()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [Iscustomer]
        else:
            permission_classes = [Isvendor]
        return [permission() for permission in permission_classes]
