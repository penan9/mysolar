# Generated by Django 3.0.6 on 2020-06-07 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200606_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='videofile',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='imagefile',
            new_name='file',
        ),
    ]