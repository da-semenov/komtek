# Generated by Django 3.2 on 2021-06-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_element_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='slug',
            field=models.SlugField(max_length=64, verbose_name='Короткое наименование'),
        ),
    ]
