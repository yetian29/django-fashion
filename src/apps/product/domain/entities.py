from dataclasses import dataclass

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
