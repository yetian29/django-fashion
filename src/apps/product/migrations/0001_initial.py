# Generated by Django 5.1.3 on 2024-11-13 08:55

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductDto",
            fields=[
                (
                    "oid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(max_length=1024)),
                ("price", models.PositiveBigIntegerField(default=0)),
            ],
            options={
                "verbose_name": "ProductDto",
            },
        ),
    ]
