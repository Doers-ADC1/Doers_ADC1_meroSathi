# Generated by Django 3.0.2 on 2020-01-21 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionPlatform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='is_favorite',
        ),
    ]