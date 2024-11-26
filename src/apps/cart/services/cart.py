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

    def update_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItem:
        cart_item_orm = self.repository.update_item_quantity(
            cart_oid, item_oid, quantity
        )
        return cart_item_orm.to_entity()

    def remove_item(self, cart_oid: UUID, item_oid: UUID) -> CartItem:
        cart_item_orm = self.repository.remove_item(cart_oid, item_oid)
        return cart_item_orm.to_entity()

    def clear_items(self, cart_oid: UUID) -> list[CartItem]:
        cart_items_orm = self.repository.clear_items(cart_oid)
        return [cart_item_orm.to_entity() for cart_item_orm in cart_items_orm]

    def increase_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItem:
        cart_item_orm = self.repository.increase_item_quantity(
            cart_oid, item_oid, quantity
        )
        return cart_item_orm.to_entity()
