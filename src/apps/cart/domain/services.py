from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import Cart, CartItem


class ICartService(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Cart:
        pass

    @abstractmethod
    def add_item(self, product: CartItem) -> CartItem:
        pass

    @abstractmethod
    def update_item(self, product_oid: UUID, qty: int) -> CartItem:
        pass

    @abstractmethod
    def remove_item(self, product_oid: UUID) -> CartItem:
        pass

    @abstractmethod
    def clear_item(self) -> list[CartItem]:
        pass

    @abstractmethod
    def increase_item_qty(self, product_oid: UUID, qty: int) -> CartItem:
        pass
