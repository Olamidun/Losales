# Generated by Django 3.1.4 on 2021-11-23 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        ('orders', '0003_auto_20211122_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.store'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='losales_commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='seller_commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
