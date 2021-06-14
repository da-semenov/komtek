from datetime import date

from django.core.exceptions import ValidationError
from django.db import models

VERSION_SYMBOLS = list('1234567890.')


def validate_version(value):
    """Проверка формата версии справочника перед сохранением в базу данных"""
    for symbol in value:
        if symbol not in VERSION_SYMBOLS or value.count('.') > 2:
            raise ValidationError(
                'Некорректный формат версии. Введите версию в формате:'
                ' `1`, `2.0`, `5.0.1`, `1.22.34`',
                params={'value': value},
            )


class Catalog(models.Model):
    """
    Модель справочника.
    """
    name = models.CharField(max_length=255,
                            verbose_name='Наименование')
    slug = models.SlugField(max_length=64,
                            verbose_name='Короткое наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    version = models.CharField(max_length=10, blank=False, null=False,
                               validators=[validate_version],
                               verbose_name='Версия справочника')
    date = models.DateField(default=date.today,
                            verbose_name='Дата начала действия')

    class Meta:
        unique_together = ('name', 'version')
        ordering = ['-date']
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return f'{self.name} ver.{self.version}'


class Element(models.Model):
    """
    Модель элемента справочника.
    """
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE,
                                related_name='catalogs',
                                verbose_name='Справочник')
    element_code = models.CharField(max_length=64, blank=False, null=False,
                                    verbose_name='Код элемента')
    element_value = models.CharField(max_length=255, blank=False, null=False,
                                     verbose_name='Значение элемента')

    class Meta:
        ordering = ['-catalog']
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'

    def __str__(self):
        return f'{self.catalog.name} - {self.element_code}'
