from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductDetailSerializer
from .models import Product
from rest_framework import status


@api_view(['GET', 'POST', 'PUT'])
def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        price = request.data.get('price')
        quantity = request.data.get('quantity')
        category_id = request.data.get('category_id')
        tags = request.data.get('tags')

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
        title = request.data.get('title')
        price = request.data.get('price')
        quantity = request.data.get('quantity')
        category_id = request.data.get('category_id')
        tags = request.data.get('tags')

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
