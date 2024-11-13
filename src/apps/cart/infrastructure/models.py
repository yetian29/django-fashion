from django.db import models

from src.apps.base.infrastructure.models import BaseDto
from src.apps.cart.domain.entities import Cart
from src.apps.product.infrastructure.models import ProductDto

# Create your models here.


class CartDto(BaseDto):
    name = models.CharField(default="Cart", editable=False)
    products = models.ManyToManyField(ProductDto)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def to_entity(self) -> Cart:
        return Cart(
            oid=self.oid,
            products=self.products,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "CartDto"
