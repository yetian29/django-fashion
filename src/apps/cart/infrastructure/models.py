from django.db import models

from src.apps.base.infrastructure.models import BaseDto
from src.apps.cart.domain.entities import Cart
from src.apps.product.infrastructure.models import ProductDto

# Create your models here.


class CartStatus(models.TextChoices):
    EMPTY = "EMPTY", "Empty Cart"
    NORMAL = "NORMAL", "Normal Cart"
    FULL = "FULL", "Full Cart"


class CartDto(BaseDto):
    name = models.CharField(default="Cart", editable=False)
    products = models.ManyToManyField(ProductDto, default=None, blank=True)
    status = models.CharField(choices=CartStatus.choices, default=CartStatus.EMPTY)
    is_active = models.BooleanField(default=False)

    MAX_PRODUCTS = 10

    def __str__(self) -> str:
        return self.name

    @property
    def cost(self) -> int:
        return sum([product.cost for product in self.products.all()])

    @property
    def count(self) -> int:
        return self.products.count()

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
            name=self.name,
            products=self.products,
            status=self.status,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "CartDto"
