from rest_framework import serializers

from .models import Category, Subcategory, Product, Gallery


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ['id', 'title', 'slug', 'category']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(source='subcategory_set', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'subcategory']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ['id', 'image', 'product']


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='subcategory.category.title')
    subcategory_name = serializers.ReadOnlyField(source='subcategory.title')
    gallery = GallerySerializer(source='gallery_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'slug', 'category_name', 'subcategory_name', 'price', 'gallery']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'subcategory', 'price', 'slug']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
