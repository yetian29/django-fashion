from datetime import datetime
from uuid import UUID

from ninja import Schema

from src.apps.product.domain.entities import Product


class ProductOutSchema(Schema):
    oid: UUID
    name: str
    description: str
    price: int
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(entity: Product) -> "ProductOutSchema":
        return ProductOutSchema(
            oid=entity.oid,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
