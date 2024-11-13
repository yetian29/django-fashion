from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import Cart
from src.apps.product.domain.entities import Product


class ICartService(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Cart:
        pass

    @abstractmethod
    def update_product_in_cart(self, product: Product) -> Product:
        pass

    @abstractmethod
    def remove_product_in_cart(self, oid: UUID) -> Product:
        pass
