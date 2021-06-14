# Generated by Django 3.2 on 2021-06-11 13:34

from django.db import migrations, models

import catalog.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_catalog_options'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='catalog',
            name='unique_version_catalog',
        ),
        migrations.AlterField(
            model_name='catalog',
            name='version',
            field=models.CharField(max_length=10, validators=[catalog.models.validate_version], verbose_name='Версия справочника'),
        ),
        migrations.AlterUniqueTogether(
            name='catalog',
            unique_together={('slug', 'version')},
        ),
    ]
