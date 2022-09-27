from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.product.models import Product, ProductType
from apps.product.serializers import ProductSerializers, ProductTypeSerializers, ProductRecommendedSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http import Http404
import requests

from apps.weather.models import WeatherType
from apps.weather.permissions import Isvendor, Iscustomer
from weather_forecast import settings


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
    permission_classes = [Isvendor, ]
    authentication_classes = [JWTAuthentication]


class ProductRecommendAPIView(APIView):
    permission_classes = [Iscustomer, ]
    authentication_classes = [JWTAuthentication, ]

    def get(self, request, pk=None, format=None):
        try:
            res = requests.get(settings.OPEN_WEATHER_URL + '&q=Dhaka').json()
        except:
            return Response({'detail': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        if res['cod'] == 200:
            temp = res["main"]['temp'] - 273.15
            weather = WeatherType.objects.filter(high_value__gte=temp, low_value__lte=temp).values_list('id', flat=True)
            products = Product.objects.filter(weather_type__in=weather)

            serializer = ProductRecommendedSerializers(products, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
