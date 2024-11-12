from dataclasses import dataclass
from uuid import UUID

from src.apps.base.domain.entities import BaseTime


@dataclass(frozen=True)
class BaseProduct:
    oid: UUID
    name: str
    price: str


@dataclass(frozen=True)
class CatalogProduct(BaseProduct):
    pass


@dataclass(frozen=True)
class Product(BaseProduct, BaseTime):
    description: str
