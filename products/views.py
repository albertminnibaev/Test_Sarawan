from rest_framework import viewsets, pagination
from rest_framework.permissions import AllowAny

from products.models import Category, Subcategory, Product, Gallery
from products.permissions import IsAdmin
from products.serializers import CategorySerializer, ProductSerializer, SubcategorySerializer, GallerySerializer, \
    ProductListSerializer


class Pagination(pagination.PageNumberPagination):
    page_size = 4


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = Pagination
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['list']:
            return [AllowAny()]
        return [IsAdmin()]


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = Pagination
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['list']:
            return [AllowAny()]
        return [IsAdmin()]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = Pagination
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['list']:
            return [AllowAny()]
        return [IsAdmin()]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductListSerializer
        return ProductSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = Pagination

    def get_permissions(self):
        if self.action in ['list']:
            return [AllowAny()]
        return [IsAdmin()]
