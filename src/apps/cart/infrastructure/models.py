from django.db import models

from src.apps.base.infrastructure.models import BaseDto
from src.apps.cart.domain.entities import Cart
from src.apps.product.infrastructure.models import ProductDto

# Create your models here.


class CartStatus(models.TextChoices):
    EMPTY = "EMPTY", "Empty Cart"
    NORMAL = "NORMAL", "Normal Cart"
    FULL = "FULL", "Full Cart"


class CartItemDto(BaseDto):
    product = models.OneToOneField(ProductDto, on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField(default=1)
    MAX_QTY = 10

    def __post_init__(self) -> None:
        self.validate_qty()

    @property
    def cost(self) -> int:
        return self.product.price * self.qty

    def validate_qty(self) -> None:
        if self.qty > 10:
            raise ValueError("Qty has to small or equal 10")


class CartDto(BaseDto):
    items = models.ManyToManyField(CartItemDto, default=None, blank=True)
    status = models.CharField(choices=CartStatus.choices, default=CartStatus.EMPTY)
    is_active = models.BooleanField(default=False)
    MAX_PRODUCTS = 10

    def __str__(self) -> str:
        return self.name

    @property
    def total_price(self) -> int:
        return sum([item.cost for item in self.items.all()])

    @property
    def total_count(self) -> int:
        return self.items.count()

    def update_status(self) -> None:
        if self.count == 0:
            self.status = CartStatus.EMPTY
        elif self.count == self.MAX_PRODUCTS:
            self.count = CartStatus.FULL
        else:
            self.count = CartStatus.NORMAL

    def to_entity(self) -> Cart:
        return Cart(
            oid=self.oid,
            items=self.items,
            status=self.status,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "CartDto"
