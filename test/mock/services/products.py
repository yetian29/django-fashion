import random
from typing import Optional
from uuid import UUID

from src.apps.product.domain.entities import CatalogProduct, Product
from src.apps.product.domain.services import IProductService
from test.mock.factories.products import CataLogProductFactory, ProductFactory


class DummyProductService(IProductService):
    def get_by_oid(self, oid: UUID) -> Product:
        return ProductFactory.build(oid=oid)

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: Optional[str] = None,
    ) -> list[CatalogProduct]:
        return [CataLogProductFactory.build() for _ in range(random.randint(0, limit))]

    def count_many(self, search: Optional[str] = None) -> int:
        return random.randint(0, 1000)
