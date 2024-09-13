from store.models import Product, Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []

