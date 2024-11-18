from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM

# Create your models here.


class ProductORM(BaseOidORM, BaseTimeORM):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "ProductORM"
