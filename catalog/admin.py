from django.contrib import admin

from catalog.models import Catalog, Element


class ElementInline(admin.TabularInline):
    model = Element
    raw_id_fields = ['catalog_id']


class CatalogAdmin(admin.ModelAdmin):
    model = Catalog
    list_display = ('pk', 'name', 'slug', 'description', 'version', 'date')
    search_fields = ('name',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'
    inlines = [ElementInline]


class ElementAdmin(admin.ModelAdmin):
    model = Element
    list_display = ('pk', 'catalog_id', 'element_code', 'element_value')
    search_fields = ('element_code',)
    list_filter = ('element_code',)


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Element, ElementAdmin)
