from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid, BaseTime
from src.apps.product.domain.entities import Product


@dataclass(frozen=True)
class Cart(BaseOid, BaseTime):
    name: str
    products: set[Product]
    is_active: bool

    @property
    def cost(self) -> int:
        return sum(product.cost for product in self.products)
