from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.weather.views import WeatherTypeViewSet

from apps.product.views import ProductTypeViewSet, ProductViewSet, ProductRecommendAPIView

router = routers.DefaultRouter()

router.register(r'product_type', ProductTypeViewSet, basename='product_type')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'weather_type', WeatherTypeViewSet, basename='weather_type')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.accounts.urls')),
    path('recommend/', ProductRecommendAPIView.as_view())

]
urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
