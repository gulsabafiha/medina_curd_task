from rest_framework import viewsets
from apps.product.models import ProductType
from apps.product.serializers import ProductTypeSerializers

from django.http import Http404


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
