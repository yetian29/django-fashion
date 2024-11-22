from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM

# Create your models here.


class UserAuthORM(BaseOidORM, BaseTimeORM):
    phone_number = models.CharField(max_length=10, null=True, default=None)
    email = models.CharField(max_length=32, null=True, default=None)
    token = models.UUIDField(null=True, default=None)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "UserAuthORM"
