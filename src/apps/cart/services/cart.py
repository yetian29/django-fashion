from dataclasses import dataclass
from uuid import UUID

from src.apps.cart.domain.entities import Cart, CartItem
from src.apps.cart.domain.services import ICartService
from src.apps.cart.infrastructure.repositories import ICartRepository


@dataclass(frozen=True)
class CartService(ICartService):
    repository: ICartRepository

    def get_or_create_cart(self, customer_oid: UUID) -> Cart:
        cart_orm = self.repository.get_or_create_cart(customer_oid)
        return cart_orm.to_entity()

    def add_item(self, cart_oid: UUID, item: CartItem) -> CartItem:
        cart_item_orm = self.repository.add_item(cart_oid, item)
        return cart_item_orm.to_entity()
