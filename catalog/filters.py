from django_filters import rest_framework as filters

from .models import Catalog, Element


class CatalogFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Catalog
        fields = ('date',)


class ElementFilter(filters.FilterSet):
    catalog = filters.CharFilter(field_name='catalog__name',
                                 lookup_expr='contains')
    version = filters.CharFilter(field_name='catalog__version',
                                 lookup_expr='exact')

    class Meta:
        model = Element
        fields = ('catalog', 'version',)


class ValidateFilter(filters.FilterSet):
    catalog = filters.CharFilter(field_name='catalog__name',
                                 lookup_expr='contains')
    code = filters.CharFilter(field_name='element_code',
                              lookup_expr='contains')
    value = filters.CharFilter(field_name='element_value',
                               lookup_expr='contains')
    date = filters.CharFilter(field_name='catalog__date',
                              lookup_expr='contains')
    version = filters.CharFilter(field_name='catalog__version',
                                 lookup_expr='contains')

    class Meta:
        model = Element
        fields = ('catalog', 'version', 'code', 'value')
