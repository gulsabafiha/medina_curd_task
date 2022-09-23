from django.urls import path 
from . import views



urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('admin_register/',views.register_admin,name="admin_register"), 
    path('customer_register/',views.register_customer,name="customer_register"), 
    path('vendor_register/',views.register_vendor,name="vendor_register"), 
]