# Generated by Django 3.0.6 on 2020-06-12 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_about_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='sequence',
            field=models.IntegerField(default=1, max_length=10),
        ),
    ]