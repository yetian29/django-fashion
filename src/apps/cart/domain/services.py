from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import Cart, CartItem


class ICartService(ABC):
    @abstractmethod
    def get_or_create(self, cart: Cart) -> Cart:
        pass

    @abstractmethod
    def add_item(self, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    def update_item(self, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    def remove_item(self, cart_oid: UUID, item_oid: UUID) -> CartItem:
        pass

    @abstractmethod
    def clear(self, cart_oid: UUID) -> list[CartItem]:
        pass

    @abstractmethod
    def increase_qty_item(self, item: CartItem) -> CartItem:
        pass
