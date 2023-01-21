from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price'.split()
        # exclude = 'text'.split()


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price created updated is_active text'.split()
