# Generated by Django 3.0.3 on 2020-03-13 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_delete_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='kind',
        ),
    ]
