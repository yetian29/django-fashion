from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import Cart


class ICartService(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Cart:
        pass
