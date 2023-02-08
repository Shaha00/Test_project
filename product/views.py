from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductDetailSerializer, ProductValidateSerializer
from .models import Product
from rest_framework import status


@api_view(['GET', 'POST', 'PUT'])
def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = serializer.validated_data.get('title')
        price = serializer.validated_data.get('price')
        quantity = serializer.validated_data.get('quantity')
        category_id = serializer.validated_data.get('category_id')
        tags = serializer.validated_data.get('tags')

        product = Product.objects.create(title=title, price=price, quantity=quantity, category_id=category_id)

        product.tags.set(tags)
        product.save()
        return Response(data=ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found '},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductDetailSerializer(product, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        price = serializer.validated_data.get('price')
        quantity = serializer.validated_data.get('quantity')
        category_id = serializer.validated_data.get('category_id')
        tags = serializer.validated_data.get('tags')

        product.title = title
        product.price = price
        product.quantity = quantity
        product.category_id = category_id
        product.tags.set(tags)
        product.save()
        return Response(data=ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
def test(request):
    # logic
    data = {
        'text': 'Hello world!',
        'int': 1000,
        'float': 9.99,
        'bool': True,
        'list': [1, 2, 3],
        'dict': {
            'list': [1, 2, 3]
        }
    }
    return Response(data=data)
