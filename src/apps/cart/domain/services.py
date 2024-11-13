from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import Cart
from src.apps.product.domain.entities import Product


class ICartService(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Cart:
        pass

    @abstractmethod
    def add_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update_product_qty(self, product_oid: UUID, qty: int) -> Product:
        pass

    @abstractmethod
    def remove_product(self, product_oid: UUID) -> Product:
        pass

    @abstractmethod
    def clear(self) -> list[Product]:
        pass

    @abstractmethod
    def increase_product_qty(product_oid: UUID, qty: int) -> Product:
        pass

    @abstractmethod
    def check_product_qty_limit() -> bool:
        pass
