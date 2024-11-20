from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.product.infrastructure.models import ProductORM


# Create your models here.
class CartStatus(models.TextChoices):
    EMPTY = "EMTY CART"
    NORMAL = "NORMAL CART"
    FULL = "FULL CART"


class CartItemORM(models.Model):
    product = models.OneToOneField(ProductORM, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def cost(self) -> int:
        return self.product.price * self.quantity

    class Meta:
        verbose_name = "CartItemORM"


class CartORM(BaseOidORM, BaseTimeORM):
    items = models.ForeignKey(CartItemORM, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    status = models.CharField(choices=CartStatus.choices, default=CartStatus.EMPTY)

    def __str__(self) -> str:
        return "Car user"

    @property
    def total_count(self) -> int:
        return [sum(item.quantity) for item in self.items]

    @property
    def total_price(self) -> int:
        return [sum(item.cost) for item in self.items]

    class Meta:
        verbose_name = "CartORM"
