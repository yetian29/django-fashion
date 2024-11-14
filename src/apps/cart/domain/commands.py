from dataclasses import dataclass
from uuid import UUID

from src.apps.product.domain.entities import CatalogProduct


@dataclass(frozen=True)
class GetCartCommand:
    oid: UUID


@dataclass(frozen=True)
class AddItemCommand:
    product: CatalogProduct


@dataclass(frozen=True)
class UpdateItemQtyCommand:
    product_oid: UUID
    qty: int


@dataclass(frozen=True)
class RemoveItemCommand:
    product_oid: UUID


@dataclass(frozen=True)
class ClearItemCommand:
    pass


@dataclass(frozen=True)
class IncreaseItemQtyCommand:
    product_oid: UUID
    qty: int
