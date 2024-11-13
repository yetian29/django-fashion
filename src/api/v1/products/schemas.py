from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema

from src.apps.base.domain.value_objects import PaginationQuery, SortOrderEnum, SortQuery
from src.apps.product.domain.commands import GetProductListCommand
from src.apps.product.domain.entities import CatalogProductSortFieldsEnum, Product


class FindQueryParams(Schema):
    search: Optional[str] = None
    sort_field: CatalogProductSortFieldsEnum = CatalogProductSortFieldsEnum.oid  # type: ignore
    sort_order: SortOrderEnum = SortOrderEnum.asc
    page: int = 0
    limit: int = 20

    def to_command(self) -> GetProductListCommand:
        return GetProductListCommand(
            search=self.search,
            sort=SortQuery(sort_field=self.sort_field.name, sort_order=self.sort_order),
            pagination=PaginationQuery(page=self.page, limit=self.limit),
        )


class ProductOutSchema(Schema):
    oid: UUID
    name: str
    description: str
    price: int
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(entity: Product) -> "ProductOutSchema":
        return ProductOutSchema(
            oid=entity.oid,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
