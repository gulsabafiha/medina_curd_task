from rest_framework import serializers
from apps.product.models import ProductType


class ProductTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['name', ]

