from dataclasses import dataclass
from uuid import UUID

from apps.base.domain.entities import BaseTime


@dataclass(frozen=True)
class BaseProduct:
    id: UUID
    name: str
    price: str


@dataclass(frozen=True)
class CatalogProduct(BaseProduct):
    pass


@dataclass(frozen=True)
class Product(BaseProduct, BaseTime):
    description: str
