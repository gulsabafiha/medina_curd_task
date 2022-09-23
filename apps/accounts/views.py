from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from apps.accounts.models import Admin, Customer, Vendor
from apps.accounts.serializers import  AdminSerializerWithToken, CustomerSerializerWithToken, UserSerializerWithToken, VendorSerializerWithToken
from rest_framework.decorators import api_view
from rest_framework.response import Response

#--------------------Admin register views----------------

@api_view(['POST'])
def register_admin(request):
    data=request.data
    try:
        user=Admin.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer=AdminSerializerWithToken(user,many=False)

        return Response(serializer.data)
    except:
        message={'detail':'User with this email already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

#------------------End Admin register------------


#-------------------Customer  Register View----------


@api_view(['POST'])
def register_customer(request):
    data=request.data
    try:
        user=Customer.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer=CustomerSerializerWithToken(user,many=False)

        return Response(serializer.data)
    except:
        message={'detail':'User with this email already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

#------------------End Customer register view------------


#-------------------Vendor and Register View----------

@api_view(['POST'])
def register_vendor(request):
    data=request.data
    try:
        user=Vendor.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer=VendorSerializerWithToken(user,many=False)

        return Response(serializer.data)
    except:
        message={'detail':'User with this email already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

#------------------End Vendor register and login view------------

#-----------------Login View-------------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer=UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k]=v
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#-------------------End Login View---------