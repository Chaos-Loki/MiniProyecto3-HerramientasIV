import django_filters
from main.models import Product 
from django.contrib.auth.models import User
from main.models import Category

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        label='Nombre del Articulo',
        lookup_expr='icontains')
    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Vendedor', 
        lookup_expr='exact')
    price = django_filters.RangeFilter(
        field_name='price', 
        label='Precio', 
        lookup_expr=['lt', 'gt'])
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Categoria',
        lookup_expr='exact'
        )

    class Meta:
        model = Product 
        fields = ['name', 'price', 'user', 'category']
