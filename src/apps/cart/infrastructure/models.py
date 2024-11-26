from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.cart.domain.entities import Cart, CartItem
from src.apps.customer.infrastructure.models import CustomerORM
from src.apps.product.infrastructure.models import ProductORM


class CartStatus(models.TextChoices):
    EMPTY = "EMPTY CART"
    NORMAL = "NORMAL CART"
    FULL = "FULL CART"


class CartORM(BaseOidORM, BaseTimeORM):
    customer = models.ForeignKey(to=CustomerORM, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(to=ProductORM, through="CartItemORM")
    is_active = models.BooleanField(default=False)
    status = models.CharField(
        max_length=16, choices=CartStatus.choices, default=CartStatus.EMPTY
    )
    MAX_CONTAINER = 15

    def update_status(self):
        items_count = self.items.count()
        if items_count > self.MAX_CONTAINER:
            self.status = CartStatus.FULL
        elif items_count == 0:
            self.status = CartStatus.EMPTY
        else:
            self.status = CartStatus.NORMAL

    @property
    def total_count(self) -> int:
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self) -> int:
        return sum(item.cost for item in self.items.all())

    def to_entity(self) -> Cart:
        return Cart(
            oid=self.oid,
            customer_oid=self.customer.oid,
            items={self.items.all()},
            total_count=self.total_count,
            total_price=self.total_price,
            is_active=self.is_active,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "CartORM"


class CartItemORM(BaseOidORM):
    cart = models.ForeignKey(
        to=CartORM, on_delete=models.CASCADE, related_name="cart_items"
    )
    product = models.ForeignKey(to=ProductORM, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    cost = models.PositiveBigIntegerField(default=0)

    def to_entity(self) -> CartItem:
        return CartItem(
            oid=self.oid,
            cart_oid=self.cart.oid,
            product=self.product,
            quantity=self.quantity,
        )

    class Meta:
        verbose_name = "CartItemORM"
        unique_together = ["cart", "product"]
