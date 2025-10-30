from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CategoryViewSet, BrandViewSet, ProductViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reviews', ReviewViewSet, basename='review')

app_name = 'products'

urlpatterns = [
    path('api/', include(router.urls)),
]
