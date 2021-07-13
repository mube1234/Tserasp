import django_filters
from .models import *
from django_filters import DateFilter, CharFilter
class MaterialFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    #end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    name = CharFilter(field_name="name", lookup_expr='icontains')
    class Meta:
        model = Material
        fields = ['name']