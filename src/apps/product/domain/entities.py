from dataclasses import dataclass, fields
from enum import Enum

from src.apps.base.domain.entities import BaseOid, BaseTime


@dataclass
class BaseProduct(BaseOid):
    name: str
    price: int


@dataclass
class CatalogProduct(BaseProduct):
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False


@dataclass
class DetailProduct(BaseProduct, BaseTime):
    description: str

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False


ProductSortFieldsEnum = Enum(
    "ProductSortFieldsEnum",
    {field.name: field.name for field in fields(CatalogProduct)},
)
