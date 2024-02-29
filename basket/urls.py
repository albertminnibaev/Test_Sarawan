from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import BasketConfig
from .views import BasketProductViewSet, BasketRetrieveAPIView, BasketUpdateAPIView

app_name = BasketConfig.name

basket_product_router = DefaultRouter()
basket_product_router.register(r'basket_product', BasketProductViewSet, basename='basket_product')

urlpatterns = [
    path('basket/', BasketRetrieveAPIView.as_view(), name='basket_get'),
    path('basket/update/', BasketUpdateAPIView.as_view(), name='basket_get'),
    path('', include(basket_product_router.urls)),
]
