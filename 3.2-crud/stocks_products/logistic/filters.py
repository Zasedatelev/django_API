import django_filters

from .models import Product


class ProductsFilter(django_filters.FilterSet):
    make = django_filters.ModelChoiceFilter(field_name="product__title",
                                            queryset=Product.objects.all())

    class Meta:
        model = Product
        fields = ('title',)
