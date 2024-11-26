from datetime import datetime
from uuid import UUID

from ninja import Schema

from src.apps.cart.domain.entities import Cart, CartItem
from src.apps.cart.domain.value_objects import CartStatusEnum


class CartOutSchema(Schema):
    oid: UUID
    customer_oid: UUID
    items: list[CartItem]
    total_count: int
    total_price: int
    is_active: bool
    status: CartStatusEnum
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def to_entity(entity: Cart) -> "CartOutSchema":
        return CartOutSchema(
            oid=entity.oid,
            customer_oid=entity.customer_oid,
            items=list(entity.items),
            total_count=entity.total_count,
            total_price=entity.total_price,
            is_active=entity.is_active,
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
