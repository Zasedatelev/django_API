from django_filters import filters
from rest_framework.viewsets import ModelViewSet
from .pagination import LargeResultsSetPagination
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
from . filters import ProductsFilter

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    search_fields = ['title', 'description']




class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductsFilter
    search_fields = ['products__title']

