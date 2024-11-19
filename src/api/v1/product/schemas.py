from datetime import datetime
from uuid import UUID

from ninja import Schema

from src.apps.base.domain.commands import (
    PaginationQueryParams,
    SortOrderEnum,
    SortQueryParams,
)
from src.apps.product.domain.commands import GetProductListCommand
from src.apps.product.domain.entities import (
    CatalogProduct,
    DetailProduct,
    ProductSortFieldsEnum,
)


class CatalogProductOutSchema(Schema):
    oid: UUID
    name: str
    price: int

    @staticmethod
    def from_entity(entity: CatalogProduct) -> "CatalogProductOutSchema":
        return CatalogProductOutSchema(
            oid=entity.oid, name=entity.name, price=entity.price
        )


class FindInQueryParams(Schema):
    search: str | None = None
    sort_field: ProductSortFieldsEnum = ProductSortFieldsEnum.oid  # type: ignore
    sort_order: SortOrderEnum = SortOrderEnum.asc
    page: int = 0
    limit: int = 20

    def to_command(self) -> GetProductListCommand:
        return GetProductListCommand(
            search=self.search,
            sort=SortQueryParams(
                sort_field=self.sort_field.name, sort_order=self.sort_order
            ),
            pagination=PaginationQueryParams(page=self.page, limit=self.limit),
        )


class DetailProductOutSchema(Schema):
    oid: UUID
    name: str
    description: str
    price: int
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(entity: DetailProduct) -> "DetailProductOutSchema":
        return DetailProductOutSchema(
            oid=entity.oid,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
