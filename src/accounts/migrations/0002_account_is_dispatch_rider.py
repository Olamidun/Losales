# Generated by Django 3.1.4 on 2021-01-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_dispatch_rider',
            field=models.BooleanField(default=False),
        ),
    ]