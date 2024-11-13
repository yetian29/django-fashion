from dataclasses import dataclass, fields
from enum import Enum
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


CatalogProductSortFieldsEnum = Enum(
    "CatalogProductSortFieldsEnum",
    {field.name: field.name for field in fields(CatalogProduct)},
)
