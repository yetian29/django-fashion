# Generated by Django 5.1.3 on 2024-11-22 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAuthORM",
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
                (
                    "phone_number",
                    models.CharField(default=None, max_length=10, null=True),
                ),
                ("email", models.CharField(default=None, max_length=32, null=True)),
                ("token", models.UUIDField(default=None, null=True)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "UserAuthORM",
            },
            bases=("base.baseoidorm", "base.basetimeorm"),
        ),
    ]
