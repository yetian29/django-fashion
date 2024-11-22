from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.product.domain.entities import CatalogProduct, DetailProduct

# Create your models here.


class ProductORM(BaseOidORM, BaseTimeORM):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    def to_detail_product_entity(self) -> DetailProduct:
        return DetailProduct(
            oid=self.oid,
            name=self.name,
            price=self.price,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def to_catalog_product_entity(self) -> CatalogProduct:
        return CatalogProduct(
            oid=self.oid,
            name=self.name,
            price=self.price,
        )

    class Meta:
        verbose_name = "ProductORM"
