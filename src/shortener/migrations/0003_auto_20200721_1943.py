# Generated by Django 3.0.8 on 2020-07-21 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20200721_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kirrurl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
