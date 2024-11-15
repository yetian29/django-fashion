from dataclasses import dataclass, fields
from enum import Enum

from src.apps.base.domain.entities import BaseOid, BaseTime


@dataclass(frozen=True)
class BaseProduct(BaseOid):
    name: str
    price: str


@dataclass(frozen=True)
class CatalogProduct(BaseProduct):
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, CatalogProduct):
            return self.oid == self.obj
        return False


@dataclass(frozen=True)
class Product(BaseProduct, BaseTime):
    description: str

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Product):
            return self.oid == self.obj
        return False


CatalogProductSortFieldsEnum = Enum(
    "CatalogProductSortFieldsEnum",
    {field.name: field.name for field in fields(CatalogProduct)},
)
