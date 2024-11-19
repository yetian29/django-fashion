from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid, BaseTime
from src.apps.cart.domain.value_objects import CartStatusEnum
from src.apps.product.domain.entities import CatalogProduct


@dataclass
class CartItem:
    product: CatalogProduct
    quantity: int


@dataclass
class Cart(BaseOid, BaseTime):
    items: set[CartItem]
    total_count: int
    total_price: int
    is_active: bool
    status: CartStatusEnum

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False
