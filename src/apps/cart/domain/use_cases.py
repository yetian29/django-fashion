from dataclasses import dataclass

from src.apps.cart.domain.commands import (
    AddItemCommand,
    ClearItemCommand,
    GetCartCommand,
    RemoveItemCommand,
    UpdateItemQtyCommand,
)
from src.apps.cart.domain.entities import Cart, CartItem
from src.apps.cart.domain.services import ICartService


@dataclass(frozen=True)
class GetCartUseCase:
    service: ICartService

    def execute(self, command: GetCartCommand) -> Cart:
        return self.service.get_by_oid(oid=command.oid)


@dataclass(frozen=True)
class AddItemUseCase:
    service: ICartService

    def execute(self, command: AddItemCommand) -> CartItem:
        return self.service.add_item(item=command.item)


@dataclass(frozen=True)
class UpdateItemQtyUseCase:
    service: ICartService

    def execute(self, command: UpdateItemQtyCommand) -> CartItem:
        return self.service.update_item(item=command.item)


@dataclass(frozen=True)
class RemoveItemQtyUseCase:
    service: ICartService

    def execute(self, command: RemoveItemCommand) -> CartItem:
        return self.service.remove_item(item_oid=command.item_oid)


@dataclass(frozen=True)
class ClearItemUseCase:
    service: ICartService

    def execute(self, command: ClearItemCommand) -> list[CartItem]:
        return self.service.clear_item()
