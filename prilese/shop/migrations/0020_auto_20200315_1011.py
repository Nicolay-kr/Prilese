# Generated by Django 3.0.3 on 2020-03-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20200314_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='kind',
        ),
        migrations.AddField(
            model_name='product',
            name='kind',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.DeleteModel(
            name='Kind',
        ),
    ]
