# Generated by Django 3.2 on 2021-06-12 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_element_catalog_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='element',
            unique_together=set(),
        ),
    ]
