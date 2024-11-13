from django.db import models

from src.apps.base.infrastructure.models import BaseDto
from src.apps.product.domain.entities import CatalogProduct, Product

# Create your models here.


class ProductDto(BaseDto):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    price = models.PositiveBigIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def cost(self) -> int:
        return self.price * self.quantity

    def __str__(self) -> str:
        return self.name

    def to_catalog_product_entity(self) -> CatalogProduct:
        return CatalogProduct(oid=self.oid, name=self.name, price=self.price)

    def to_product_entity(self) -> Product:
        return Product(
            oid=self.oid,
            name=self.name,
            price=self.price,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "ProductDto"
