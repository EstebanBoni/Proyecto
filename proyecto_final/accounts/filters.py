import django_filters
from django_filters import DateFilter
from django.forms import widgets
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type =  'date'

class GastoFilter(django_filters.FilterSet):
    fecha_inicio = DateFilter(field_name="fecha_gasto", lookup_expr='gte', widget=DateInput)
    fecha_fin = DateFilter(field_name="fecha_gasto", lookup_expr='lte', widget=DateInput)
    class Meta:
        model = Gasto
        fields = '__all__'
        exclude = ['fecha_gasto']
