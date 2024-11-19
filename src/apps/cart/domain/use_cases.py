from dataclasses import dataclass

from src.apps.cart.domain.commands import (
    AddItemCommand,
    ClearItemsCommand,
    CreateCartCommand,
    GetCartCommand,
    RemoveItemCommand,
    UpdateItemCommand,
)
from src.apps.cart.domain.entities import Cart, CartItem
from src.apps.cart.domain.services import ICartService


@dataclass(frozen=True)
class GetCartUseCase:
    service: ICartService

    def execute(self, command: GetCartCommand) -> Cart:
        return self.service.get_cart_by_oid(oid=command.oid)


@dataclass(frozen=True)
class CreateCartUseCase:
    service: ICartService

    def execute(self, command: CreateCartCommand) -> Cart:
        return self.service.create_cart(cart=command.cart)


@dataclass(frozen=True)
class AddItemUseCase:
    service: ICartService

    def execute(self, command: AddItemCommand) -> CartItem:
        return self.service.add_item(cart_oid=command.oid, item=command.item)


@dataclass(frozen=True)
class UpdateItemUseCase:
    service: ICartService

    def execute(self, command: UpdateItemCommand) -> CartItem:
        return self.service.update_item(cart_oid=command.oid, item=command.item)


@dataclass(frozen=True)
class RemoveItemUseCase:
    service: ICartService

    def execute(self, command: RemoveItemCommand) -> CartItem:
        return self.service.remove_item(cart_oid=command.oid, item_oid=command.item_oid)


@dataclass(frozen=True)
class ClearItemsUseCase:
    service: ICartService

    def execute(self, command: ClearItemsCommand) -> list[CartItem]:
        return self.service.clear_items(cart_oid=command.cart_oid)
