from dataclasses import dataclass
from uuid import UUID

from src.apps.cart.domain.entities import Cart
from src.apps.cart.domain.services import ICartService
from src.apps.cart.infrastructure.repositories import ICartRepository


@dataclass(frozen=True)
class CartService(ICartService):
    repository: ICartRepository

    def get_or_create_cart(self, customer_oid: UUID) -> Cart:
        return self.repository.get_or_create_cart(customer_oid)
