from rest_framework import viewsets, filters
from store.models import Product, Category
from store.serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    '''
        ViewSet description:
        - Endpoint for Product CRUD

        Sort fields:
        - name: Allows you to sort by name.
        - category: Allows you to sort by name.
        - value: Allows you to sort by value.

        Seach fields:
        - name: Allows you to search the result by name.
        - value: Allows you to search the result by value.

        Allowed HTTP Methods:
        - ALL
        
        Serializer Class:
        - ProductSerializer: used for data serialization and deserialization.
    '''

    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields  = ['name', 'value']
    ordering_fields = ['name', 'category', 'value']

class CategoryViewSet(viewsets.ModelViewSet):
    '''
        ViewSet description:
        - Endpoint for Category CRUD

        Sort fields:
        - name: Allows you to sort by name.

        Seach fields:
        - name: Allows you to search the result by name.

        Allowed HTTP Methods:
        - ALL
        
        Serializer Class:
        - CategorySerializer: used for data serialization and deserialization.
    '''

    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields  = ['name']
    ordering_fields = ['name']

    

