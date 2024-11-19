# Generated by Django 5.1.3 on 2024-11-19 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductORM",
            fields=[
                (
                    "basetimeorm_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="base.basetimeorm",
                    ),
                ),
                (
                    "baseoidorm_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.baseoidorm",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(max_length=1024)),
                ("price", models.PositiveBigIntegerField(default=0)),
            ],
            options={
                "verbose_name": "ProductORM",
            },
            bases=("base.baseoidorm", "base.basetimeorm"),
        ),
    ]
