# Generated by Django 3.2 on 2021-06-11 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_catalog_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='catalog',
            unique_together={('name', 'version')},
        ),
    ]