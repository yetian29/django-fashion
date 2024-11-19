from dataclasses import dataclass
from uuid import UUID

from src.apps.product.domain.entities import CatalogProduct, DetailProduct
from src.apps.product.domain.errors import (
    ProductIsNotFoundException,
    ProductsAreNotFoundException,
)
from src.apps.product.domain.services import IProductService
from src.apps.product.infrastructure.repositories import IProductRepository
from src.helper import fail


@dataclass(frozen=True)
class ProductService(IProductService):
    repository: IProductRepository

    def get_by_oid(self, oid: UUID) -> DetailProduct:
        product_orm = self.repository.get_by_oid(oid)
        if not product_orm:
            fail(ProductIsNotFoundException)
        return product_orm.to_detail_product_entity()

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None,
    ) -> list[CatalogProduct]:
        products_orm = self.repository.find_many(
            sort_field, sort_order, limit, offset, search
        )
        if not products_orm:
            fail(ProductsAreNotFoundException)
        return [product.to_catalog_product_entity() for product in products_orm]

    def count_many(self, search: str | None = None) -> int:
        count = self.repository.count_many(search)
        if not count:
            fail(ProductsAreNotFoundException)
        return count
