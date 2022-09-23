from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken 
from apps.accounts.models import Admin, Customer, Vendor
from django.contrib.auth import get_user_model

User=get_user_model()

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=['id','username','email']

class AdminSerializerWithToken(AdminSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Admin
        fields=['id','username','email','token']

    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','username','email']

class CustomerSerializerWithToken(CustomerSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Customer
        fields=['id','username','email','token']

    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=['id','username','email']

class VendorSerializerWithToken(VendorSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Vendor
        fields=['id','username','email','token']

    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']


class UserSerializerWithToken(UserSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','token']

    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)