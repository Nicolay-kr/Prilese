# Generated by Django 3.0.3 on 2020-03-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20200328_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=100),
        ),
    ]
