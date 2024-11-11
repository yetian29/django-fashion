from dataclasses import dataclass
from uuid import uuid4

from apps.base.domain.entities import BaseTime
from apps.product.domain.value_objects import (
    ProductDescription,
    ProductId,
    ProductName,
    ProductPrice,
)


@dataclass(frozen=True)
class BaseProduct:
    id: ProductId
    name: ProductName
    price: ProductPrice

    def __post_init__(self) -> None:
        if not self.id:
            self.id = ProductId(value=uuid4())


@dataclass(frozen=True)
class CatalogProduct(BaseProduct):
    pass


@dataclass(frozen=True)
class Product(BaseProduct, BaseTime):
    description: ProductDescription
