from dataclasses import dataclass
from uuid import UUID

from src.apps.base.helper.errors import fail
from src.apps.cart.domain.entities import Cart
from src.apps.cart.domain.errors import CartIsNotFoundException
from src.apps.cart.domain.services import ICartService
from src.apps.cart.infrastructure.repositories import ICartRepository


@dataclass(frozen=True)
class CartService(ICartService):
    repository: ICartRepository

    def get_by_oid(self, oid: UUID) -> Cart:
        dto = self.repository.get_by_oid(oid)
        if not dto:
            fail(CartIsNotFoundException)
        return dto.to_entity()
