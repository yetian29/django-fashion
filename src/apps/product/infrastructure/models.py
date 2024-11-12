from django.db import models

from src.apps.base.infrastructure.models import BaseDto
from src.apps.product.domain.entities import CatalogProduct, Product

# Create your models here.


class ProductDto(BaseDto):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    price = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name = "ProductDto"

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_entity(self, entity: Product) -> "BaseDto":
        return BaseDto(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_catalog_product_entity(self) -> CatalogProduct:
        return CatalogProduct(id=self.id, name=self.name, price=self.price)

    def to_product_entity(self) -> Product:
        return Product(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
