# Generated by Django 3.0.6 on 2020-06-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200604_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='filename',
        ),
        migrations.AddField(
            model_name='home',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
