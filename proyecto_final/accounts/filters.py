import django_filters
from django_filters import DateFilter
from .models import *

class GastoFilter(django_filters.FilterSet):
    fecha_inicio = DateFilter(field_name="fecha_gasto", lookup_expr='gte')
    fecha_fin = DateFilter(field_name="fecha_gasto", lookup_expr='lte')
    class Meta:
        model = Gasto
        fields = '__all__'
        exclude = ['fecha_gasto']
