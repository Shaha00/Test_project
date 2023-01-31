from rest_framework import serializers
from .models import Product, Category, Tag, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # tags = TagSerializer(many=True)
    tag_list = serializers.SerializerMethodField()
    product_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id product_reviews title price category tag_list'.split()
        # exclude = 'text'.split()

    def get_tag_list(self, product_object):
        # tags = product_object.tags.all()
        # list_ = []
        # for i in tags:
        #     list_.append(i.name)
        # return list_
        return [i.name for i in product_object.tags.all()]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id category tags title price created updated is_active text'.split()
