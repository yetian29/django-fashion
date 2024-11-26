from dataclasses import dataclass

from src.apps.cart.domain.commands import (
    AddItemCommand,
    ClearItemsCommand,
    GetOrCreateCartCommand,
    IncreaseItemQuantityCommand,
    RemoveItemCommand,
    UpdateItemQuantityCommand,
)
from src.apps.cart.domain.entities import Cart, CartItem
from src.apps.cart.domain.services import ICartService


@dataclass(frozen=True)
class GetOrCreateCartUseCase:
    service: ICartService

    def execute(self, command: GetOrCreateCartCommand) -> Cart:
        return self.service.get_or_create_cart(customer_oid=command.customer_oid)


@dataclass(frozen=True)
class AddItemUseCase:
    service: ICartService

    def execute(self, command: AddItemCommand) -> CartItem:
        return self.service.add_item(cart_oid=command.cart_oid, item=command.item)


@dataclass(frozen=True)
class UpdateItemQuantityUseCase:
    service: ICartService

    def execute(self, command: UpdateItemQuantityCommand) -> CartItem:
        return self.service.update_item_quantity(
            cart_oid=command.cart_oid,
            item_oid=command.item_oid,
            quantity=command.quantity,
        )


@dataclass(frozen=True)
class RemoveItemUseCase:
    service: ICartService

    def execute(self, command: RemoveItemCommand) -> CartItem:
        return self.service.remove_item(
            cart_oid=command.cart_oid, item_oid=command.item_oid
        )


@dataclass(frozen=True)
class ClearItemsUseCase:
    service: ICartService

    def execute(self, command: ClearItemsCommand) -> list[CartItem]:
        return self.service.clear_items(cart_oid=command.cart_oid)


@dataclass(frozen=True)
class IncreaseItemQuantityUseCase:
    service: ICartService

    def execute(self, command: IncreaseItemQuantityCommand) -> CartItem:
        return self.service.increase_item_quantity(
            cart_oid=command.cart_oid,
            item_oid=command.item_oid,
            quantity=command.quantity,
        )
