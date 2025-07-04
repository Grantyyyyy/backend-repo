from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet


app_name = 'customer_module'

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(router.urls)),
]


