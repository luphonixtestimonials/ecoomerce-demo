from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CouponViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'coupons', CouponViewSet, basename='coupon')
router.register(r'orders', OrderViewSet, basename='order')

app_name = 'orders'

urlpatterns = [
    path('api/', include(router.urls)),
]
