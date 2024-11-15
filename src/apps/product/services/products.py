from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from src.apps.base.helper.errors import fail
from src.apps.product.domain.entities import CatalogProduct, Product
from src.apps.product.domain.errors import (
    ProductIsNotFoundException,
    ProductsAreNotFoundException,
)
from src.apps.product.domain.services import IProductService
from src.apps.product.infrastructure.repositories import IProductRepository


@dataclass(frozen=True)
class ProductService(IProductService):
    repository: IProductRepository

    def get_by_oid(self, oid: UUID) -> Product:
        dto = self.repository.get_by_oid(oid)
        if not dto:
            fail(ProductIsNotFoundException)
        return dto.to_product_entity()

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: Optional[str] = None,
    ) -> list[CatalogProduct]:
        products = self.repository.find_many(
            sort_field, sort_order, limit, offset, search
        )
        if not products:
            fail(ProductsAreNotFoundException)
        return [product.to_catalog_product_entity() for product in products]

    def count_many(self, search: Optional[str] = None) -> int:
        count = self.repository.count_many(search)
        if not count:
            fail(ProductsAreNotFoundException)
        return count
