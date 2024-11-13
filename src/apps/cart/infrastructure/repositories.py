from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from src.apps.cart.infrastructure.models import CartDto


class ICartRepository(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Optional[CartDto]:
        pass


class PostgresCartRepository(ICartRepository):
    def get_by_oid(self, oid: UUID) -> Optional[CartDto]:
        return CartDto.objects.get(oid=oid)
