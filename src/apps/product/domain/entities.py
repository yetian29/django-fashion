from dataclasses import dataclass, fields
from datetime import datetime
from enum import Enum
from uuid import UUID


@dataclass
class BaseProduct:
    oid: UUID
    name: str
    price: int


@dataclass
class CatalogProduct(BaseProduct):
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False


@dataclass
class DetailProduct(BaseProduct):
    description: str
    created_at: datetime
    updated_at: datetime

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False


ProductSortFieldsEnum = Enum(
    "ProductSortFieldsEnum",
    {field.name: field.name for field in fields(CatalogProduct)},
)
