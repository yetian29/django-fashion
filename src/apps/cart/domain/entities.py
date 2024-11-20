from dataclasses import dataclass
from uuid import UUID

from src.apps.base.domain.entities import BaseOid, BaseTime
from src.apps.cart.domain.value_objects import CartStatusEnum
from src.apps.product.domain.entities import CatalogProduct


@dataclass
class Cart(BaseOid, BaseTime):
    total_count: int
    total_price: int
    is_active: bool
    status: CartStatusEnum

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False


@dataclass
class CartItem(BaseOid):
    cart_oid: UUID
    product: CatalogProduct
    quantity: int

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False
