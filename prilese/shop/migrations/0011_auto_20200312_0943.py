# Generated by Django 3.0.3 on 2020-03-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kind',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]