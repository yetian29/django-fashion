from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid, BaseTime
from src.apps.cart.domain.value_objects import CartStatusEnum
from src.apps.product.domain.entities import Product


@dataclass(frozen=True)
class Cart(BaseOid, BaseTime):
    name: str
    products: set[Product]
    cost: int
    status: CartStatusEnum
    is_active: bool
