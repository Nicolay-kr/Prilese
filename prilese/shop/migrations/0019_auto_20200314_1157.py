# Generated by Django 3.0.3 on 2020-03-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200314_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='kind',
        ),
        migrations.AddField(
            model_name='product',
            name='kind',
            field=models.ManyToManyField(blank=True, related_name='product', to='shop.Kind'),
        ),
    ]
