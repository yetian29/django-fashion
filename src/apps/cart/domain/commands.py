from dataclasses import dataclass
from uuid import UUID

from src.apps.cart.domain.entities import Cart, CartItem


@dataclass(frozen=True)
class GetOrCreateCartCommand:
    cart: Cart


@dataclass(frozen=True)
class AddItemCommand:
    cart_oid: UUID
    item: CartItem


@dataclass(frozen=True)
class UpdateItemCommand:
    cart_oid: UUID
    item_oid: UUID
    quantity: int


@dataclass(frozen=True)
class RemoveItemCommand:
    cart_oid: UUID
    item_oid: UUID


@dataclass(frozen=True)
class ClearItemsCommand:
    cart_oid: UUID


@dataclass(frozen=True)
class IncreaseQtyItemCommand:
    cart_oid: UUID
    item_oid: UUID
    quantity: int
