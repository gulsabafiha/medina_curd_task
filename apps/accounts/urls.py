from django.urls import path 
from . import views



urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('admin_register/',views.registerAdmin,name="admin_register"), 
    path('customer_register/',views.registerCustomer,name="customer_register"), 
    path('vendor_register/',views.registerVendor,name="vendor_register"), 
]