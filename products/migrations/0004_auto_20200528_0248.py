# Generated by Django 2.2.6 on 2020-05-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_fuel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/products'),
        ),
    ]
