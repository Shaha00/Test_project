from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductDetailSerializer
from .models import Product
from rest_framework import status


@api_view(['GET'])
def products_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found '},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductDetailSerializer(product, many=False)
    return Response(data=serializer.data)


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
