# Generated by Django 2.2.7 on 2020-06-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_product_youtubeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='youtubeID',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
