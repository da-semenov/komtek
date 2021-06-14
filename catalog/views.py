from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from catalog.filters import CatalogFilter, ElementFilter, ValidateFilter
from catalog.models import Catalog, Element
from catalog.serializers import CatalogSerializer, ElementSerializer


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение всех справочников или актуальных на указанную дату."""
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = CatalogFilter
    search_fields = ['name', ]


class ElementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Получение элементов заданного справочника текущей версии или
    указанной версии.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ElementFilter
    filterset_fields = ('catalog', 'version',)


class ValidateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Проверка наличия элементов заданного справочника текущей версии
    или указанной версии.
    Запрос возвращает пустой список если элемент не найден.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ValidateFilter
    filterset_fields = ('catalog', 'version', 'code', 'value')
