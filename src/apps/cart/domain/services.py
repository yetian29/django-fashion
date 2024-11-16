from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import Cart, CartItem


class ICartService(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Cart:
        pass

    @abstractmethod
    def add_item(self, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    def update_item(self, item: CartItem) -> CartItem:
        pass

    @abstractmethod
    def remove_item(self, item_oid: UUID) -> CartItem:
        pass

    @abstractmethod
    def clear_item(self) -> list[CartItem]:
        pass
