from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.apps.cart.domain.value_objects import CartStatusEnum
from src.apps.product.domain.entities import CatalogProduct


@dataclass
class Cart:
    oid: UUID
    total_count: int
    total_price: int
    is_active: bool
    status: CartStatusEnum
    created_at: datetime
    updated_at: datetime

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False


@dataclass
class CartItem:
    oid: UUID
    cart_oid: UUID
    product: CatalogProduct
    quantity: int

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False
