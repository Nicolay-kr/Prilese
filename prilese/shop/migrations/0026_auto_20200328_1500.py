# Generated by Django 3.0.3 on 2020-03-28 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total',
            new_name='quantity',
        ),
    ]
