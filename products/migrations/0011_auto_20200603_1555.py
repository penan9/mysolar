# Generated by Django 3.0.6 on 2020-06-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200603_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
