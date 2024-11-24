from dataclasses import dataclass

from src.apps.cart.domain.commands import (
    AddItemCommand,
    ClearItemsCommand,
    GetOrCreateCartCommand,
    IncreaseQtyItemCommand,
    RemoveItemCommand,
    UpdateItemCommand,
)
from src.apps.cart.domain.entities import Cart, CartItem
from src.apps.cart.domain.services import ICartService


@dataclass(frozen=True)
class GetOrCreateCartUseCase:
    service: ICartService

    def execute(self, command: GetOrCreateCartCommand) -> Cart:
        return self.service.get_or_create(cart=command.cart)


@dataclass(frozen=True)
class AddItemUseCase:
    service: ICartService

    def execute(self, command: AddItemCommand) -> CartItem:
        return self.service.add_item(cart_oid=command.cart_oid, item=command.item)


@dataclass(frozen=True)
class UpdateItemUseCase:
    service: ICartService

    def execute(self, command: UpdateItemCommand) -> CartItem:
        return self.service.update_item(
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
class IncreaseQtyItemUseCase:
    service: ICartService

    def execute(self, command: IncreaseQtyItemCommand) -> CartItem:
        return self.service.increase_qty_item(
            cart_oid=command.cart_oid,
            item_oid=command.item_oid,
            quantity=command.quantity,
        )
