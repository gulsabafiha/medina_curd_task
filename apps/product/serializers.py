from rest_framework import serializers
from apps.product.models import ProductType, Product


class ProductTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['name', ]


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity']


class ProductRecommendedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'product_type', 'weather_type']
