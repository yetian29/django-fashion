from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from apps.product.domain.entities import Product


class IProductService(ABC):
    @abstractmethod
    def get_by_id(self, id: UUID) -> Product:
        pass

    @abstractmethod
    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: Optional[str] = None,
    ) -> list[Product]:
        pass

    @abstractmethod
    def count_many(self, search: Optional[str] = None) -> int:
        pass
