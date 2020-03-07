# Generated by Django 3.0.3 on 2020-03-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]
