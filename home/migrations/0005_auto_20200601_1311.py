# Generated by Django 3.0.6 on 2020-06-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200528_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='videofile',
            field=models.FileField(blank=True, default='', upload_to='video/home', verbose_name=''),
        ),
    ]
