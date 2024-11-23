from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.apps.cart.domain.value_objects import CartStatusEnum
from src.apps.product.domain.entities import CatalogProduct


@dataclass
class CartItem:
    oid: UUID
    cart_oid: UUID
    product: CatalogProduct
    quantity: int

    @property
    def cost(self) -> int:
        return self.product.price * self.quantity

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, self.__class__):
            return self.oid == obj.oid
        return False


@dataclass
class Cart:
    oid: UUID
    customer_oid: UUID
    items: set[CartItem]
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
