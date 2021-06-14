from rest_framework import serializers

from catalog.models import Catalog, Element


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):
    catalog = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Element
        fields = ('id', 'element_code', 'element_value', 'catalog')
