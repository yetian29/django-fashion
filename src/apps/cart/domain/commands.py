from dataclasses import dataclass
from uuid import UUID

from src.apps.cart.domain.entities import CartItem


@dataclass(frozen=True)
class GetCartCommand:
    oid: UUID


@dataclass(frozen=True)
class AddItemCommand:
    item: CartItem


@dataclass(frozen=True)
class UpdateItemQtyCommand:
    item: CartItem


@dataclass(frozen=True)
class RemoveItemCommand:
    item_oid: UUID


@dataclass(frozen=True)
class ClearItemCommand:
    pass
