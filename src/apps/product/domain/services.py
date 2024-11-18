from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.product.domain.entities import CatalogProduct, DetailProduct


class IProductService(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> DetailProduct:
        pass

    @abstractmethod
    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None,
    ) -> list[CatalogProduct]:
        pass

    @abstractmethod
    def count_many(self, search: str | None = None) -> int:
        pass
