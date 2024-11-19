import random
from uuid import UUID

from src.apps.product.domain.entities import DetailProduct
from src.apps.product.domain.services import IProductService
from test.mock.factory.product import DetailProductFactory


class DummyProductService(IProductService):
    def get_by_oid(self, oid: UUID) -> DetailProduct:
        return DetailProductFactory.build(oid=oid)

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None,
    ) -> list[DetailProduct]:
        return [DetailProductFactory.build() for _ in range(random.randint(0, limit))]

    def count_many(self, search: str | None = None):
        return random.randint(0, 1000)
