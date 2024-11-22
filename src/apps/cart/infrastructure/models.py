from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.product.infrastructure.models import ProductORM


# Create your models here.
class CartStatus(models.TextChoices):
    EMPTY = "EMTY CART"
    NORMAL = "NORMAL CART"
    FULL = "FULL CART"


class CartORM(BaseOidORM, BaseTimeORM):
    is_active = models.BooleanField(default=False)
    status = models.CharField(
        max_length=16, choices=CartStatus.choices, default=CartStatus.EMPTY
    )

    def __str__(self) -> str:
        return "Car user"

    @property
    def total_count(self) -> int:
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self) -> int:
        return sum(item.cost for item in self.items.all())

    class Meta:
        verbose_name_plural = "CartORM"


class CartItemORM(BaseOidORM):
    cart = models.ForeignKey(CartORM, on_delete=models.PROTECT, related_name="items")
    product = models.OneToOneField(ProductORM, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def cost(self) -> int:
        return self.product.price * self.quantity

    class Meta:
        verbose_name = "CartItemORM"
