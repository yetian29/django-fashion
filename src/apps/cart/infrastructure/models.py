from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.customer.infrastructure.models import CustomerORM
from src.apps.product.infrastructure.models import ProductORM


class CartStatus(models.TextChoices):
    EMPTY = "EMPTY CART"
    NORMAL = "NORMAL CART"
    FULL = "FULL CART"


class CartORM(BaseOidORM, BaseTimeORM):
    customer = models.ForeignKey(to=CustomerORM, on_delete=models.CASCADE)
    items = models.ManyToManyField(
        to=ProductORM, through="CartItemORM", on_delte=models.PROTECT
    )
    is_active = models.BooleanField(default=False)
    status = models.CharField(choices=CartStatus.choices, default=CartStatus.EMPTY)
    MAX_CONTAINER = 15

    def update_status(self):
        if len(self.items.all()) > self.MAX_CONTAINER:
            self.status = CartStatus.FULL
        elif len(self.items.all()) == 0:
            self.status = CartStatus.EMPTY
        else:
            self.status = CartStatus.NORMAL

    @property
    def total_count(self) -> int:
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self) -> int:
        return sum(item.cost for item in self.items.all())


class CartItemORM(BaseOidORM):
    cart = models.ForeignKey(to=CartORM, on_delete=models.CASCADE)
    product = models.OneToOneField(to=ProductORM, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def cost(self) -> int:
        return self.product.price * self.quantity

    class Meta:
        verbose_name = "CartItemORM"
