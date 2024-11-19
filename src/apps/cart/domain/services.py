from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import Cart, CartItem


class ICartService(ABC):
    @abstractmethod
    def get_cart_by_oid(self, oid: UUID) -> Cart:
        pass

    @abstractmethod
    def create_cart(self, cart: Cart) -> Cart:
        pass

    @abstractmethod
    def add_item(self, cart_oid: UUID, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    def update_item(self, cart_oid: UUID, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    def remove_item(self, cart_oid: UUID, item_oid: UUID) -> CartItem:
        pass

    @abstractmethod
    def clear_items(self, cart_oid: UUID) -> list[CartItem]:
        pass
