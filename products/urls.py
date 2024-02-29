from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import NestedSimpleRouter

from .apps import ProductsConfig
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet, GalleryViewSet

app_name = ProductsConfig.name

category_router = DefaultRouter()
category_router.register(r'category', CategoryViewSet, basename='category')
subcategory_router = DefaultRouter()
subcategory_router.register(r'subcategory', SubcategoryViewSet, basename='subcategory')
product_router = DefaultRouter()
product_router.register(r'product', ProductViewSet, basename='product')
gallery_router = DefaultRouter()
gallery_router.register(r'gallery', GalleryViewSet, basename='gallery')
# subcategory_router = NestedSimpleRouter(category_router, r'category', lookup='category')
# subcategory_router.register("subcategory", SubcategoryViewSet, basename='category')

urlpatterns = [
    path('', include(category_router.urls)),
    path('', include(subcategory_router.urls)),
    path('', include(product_router.urls)),
    path('', include(gallery_router.urls)),
]
