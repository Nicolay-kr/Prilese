# Generated by Django 3.0.3 on 2020-03-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_auto_20200329_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='goods',
        ),
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ManyToManyField(to='shop.Cart'),
        ),
    ]
