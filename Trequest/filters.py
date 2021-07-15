import django_filters
from .models import *
from django_filters import DateFilter, CharFilter


class MaterialFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Material
        fields = ['name']



class UserFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr='icontains')

    class Meta:
        model = MyUser
        fields = ['first_name']
