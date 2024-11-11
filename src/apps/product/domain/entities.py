

from dataclasses import dataclass
from apps.base.domain.entities import BaseEntity

@dataclass
class Product(BaseEntity):
    name: str
    description: str
    price: int
    
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Product):
            return obj.oid == self.oid
        return False
    