from abc import ABC, abstractmethod
from typing import Iterable, Optional
from uuid import UUID

from django.db.models import Q

from src.apps.product.infrastructure.models import ProductDto


class IProductRepository(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Optional[ProductDto]:
        pass

    @abstractmethod
    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: Optional[str] = None,
    ) -> Optional[Iterable[ProductDto]]:
        pass

    @abstractmethod
    def count_many(self, search: Optional[str] = None) -> Optional[int]:
        pass


class PostgresProductRepository(IProductRepository):
    def get_by_id(self, id: UUID) -> Optional[ProductDto]:
        return ProductDto.objects.get(id)

    def _build_find_query(search: Optional[str] = None) -> Q:
        query = Q()
        if search:
            search_query = ProductDto.objects.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
            query &= search_query
        return query

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: Optional[str] = None,
    ) -> Optional[Iterable[ProductDto]]:
        query = self._build_find_query(search)
        order = "-" if sort_order == -1 else ""
        sort_by_field = f"{order}{sort_field}"
        products = ProductDto.objects.filter(query).order_by(sort_by_field)[
            offset : offset + limit
        ]
        if not products:
            return None

        for product in products:
            yield from product

    def count_many(self, search: Optional[str] = None) -> Optional[int]:
        query = self._build_find_query(search)
        return ProductDto.objects.filter(query).count()
