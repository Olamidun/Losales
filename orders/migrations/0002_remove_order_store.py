# Generated by Django 3.1.4 on 2021-11-22 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='store',
        ),
    ]
