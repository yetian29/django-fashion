from abc import ABC, abstractmethod
from uuid import UUID

from django.db.models import Q

from src.apps.product.infrastructure.models import ProductORM


class IProductRepository(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> ProductORM | None:
        pass

    @abstractmethod
    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None,
    ) -> list[ProductORM] | None:
        pass

    @abstractmethod
    def count_many(self, search: str | None = None) -> int | None:
        pass


class PostgresProductRepository(IProductRepository):
    def get_by_oid(self, oid: UUID) -> ProductORM | None:
        return ProductORM.objects.get(oid=oid)

    def _build_find_query(self, search: str | None = None) -> Q:
        query = Q()
        if search:
            search_query = Q(name__icontains=search) | Q(description__icontains=search)
            query &= search_query
        return query

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None,
    ) -> list[ProductORM] | None:
        query = self._build_find_query(search)
        sort_direction = "" if sort_order == 1 else "-"
        sort_by_field = f"{sort_direction}{sort_field}"
        products = ProductORM.objects.filter(query).order_by(sort_by_field)[
            offset : offset + limit
        ]
        return list(products) if products else None

    def count_many(self, search: str | None = None) -> int | None:
        query = self._build_find_query(search)
        return ProductORM.objects.filter(query).count()
