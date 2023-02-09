from rest_framework import serializers
from .models import Product, Category, Tag, Review
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()


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


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=1000)
    price = serializers.FloatField(min_value=1, max_value=1000000)
    quantity = serializers.IntegerField(default=0)
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField(
        min_value=1
    ))

    def validate_category_id(self, category_id):  # 100
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError(f"Category with ({category_id}) does not exists")
        return category_id

    def validate_tags(self, tags):
        tags_id = set(i[0] for i in Tag.objects.all().values_list('id'))
        invalid_tags = set(tags).difference(tags_id)
        if invalid_tags:
            raise ValidationError(f"Category with ({', '.join(map(str, invalid_tags))}) does not exists")
        return tags

