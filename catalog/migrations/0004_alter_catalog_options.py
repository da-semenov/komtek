# Generated by Django 3.2 on 2021-06-11 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_catalog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'ordering': ['-date'], 'verbose_name': 'Справочник', 'verbose_name_plural': 'Справочники'},
        ),
    ]
