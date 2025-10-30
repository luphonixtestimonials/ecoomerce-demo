from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CartViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')

app_name = 'cart'

urlpatterns = [
    path('api/', include(router.urls)),
]
