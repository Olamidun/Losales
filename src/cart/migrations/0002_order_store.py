# Generated by Django 3.1.4 on 2021-01-05 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210104_1223'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]