from dataclasses import dataclass
from uuid import UUID

from src.apps.cart.domain.entities import Cart, CartItem


@dataclass(frozen=True)
class GetOrCreateCartCommand:
    cart: Cart


@dataclass(frozen=True)
class AddItemCommand:
    item: CartItem


@dataclass(frozen=True)
class UpdateItemCommand:
    item: CartItem


@dataclass(frozen=True)
class RemoveItemCommand:
    item: CartItem


@dataclass(frozen=True)
class ClearItemsCommand:
    cart_oid: UUID


@dataclass(frozen=True)
class IncreaseQtyItemCommand:
    item: CartItem
