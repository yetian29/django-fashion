from dataclasses import dataclass
from uuid import UUID

from src.apps.product.domain.entities import Product


@dataclass(frozen=True)
class GetCartCommand:
    oid: UUID


@dataclass(frozen=True)
class AddProductCommand:
    product: Product


@dataclass(frozen=True)
class UpdateProductQtyCommand:
    product_oid: UUID
    qty: int


@dataclass(frozen=True)
class RemoveProductCommand:
    product_oid: UUID


@dataclass(frozen=True)
class ClearCartCommand:
    pass


@dataclass(frozen=True)
class IncreaseProductQtyCommand:
    product_oid: UUID
    qty: int
