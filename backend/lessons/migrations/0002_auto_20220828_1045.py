# Generated by Django 3.2.9 on 2022-08-28 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='age',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='difficulty',
        ),
    ]
