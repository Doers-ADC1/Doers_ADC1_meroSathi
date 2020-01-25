# Generated by Django 3.0.2 on 2020-01-25 05:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questionPlatform', '0004_auto_20200125_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='commented_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
