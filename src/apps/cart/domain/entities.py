from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid, BaseTime
from src.apps.base.domain.value_objects import Qty
from src.apps.cart.domain.value_objects import CartStatusEnum
from src.apps.product.domain.entities import CatalogProduct


@dataclass(frozen=True)
class CartItem(BaseOid):
    product: CatalogProduct
    qty: Qty


@dataclass(frozen=True)
class Cart(BaseOid, BaseTime):
    items: set[CartItem]
    total_count: int
    total_price: int
    status: CartStatusEnum
