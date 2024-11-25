# Generated by Django 5.1.3 on 2024-11-25 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartorm_options_cartorm_customer_cartorm_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemorm',
            name='cost',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartitemorm',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cart.cartorm'),
        ),
    ]