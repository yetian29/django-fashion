from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid, BaseTime
from src.apps.product.domain.entities import Product


@dataclass
class Cart(BaseOid, BaseTime):
    items: set[Product]
    is_active: bool
