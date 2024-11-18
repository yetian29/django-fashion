from dataclasses import dataclass
from uuid import UUID

from src.apps.product.domain.entities import DetailProduct
from src.apps.product.domain.services import IProductService
from src.apps.product.infrastructure.repositories import IProductRepository


@dataclass(frozen=True)
class ProductService(IProductService):
    repository: IProductRepository

    def get_by_oid(self, oid: UUID) -> DetailProduct:
        pass

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None,
    ):
        pass

    def count_many(self, search: str | None = None):
        pass
