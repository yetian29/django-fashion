from dataclasses import dataclass, field
from uuid import UUID

from src.apps.base.domain.commands import PaginationQueryParams, SortQueryParams


@dataclass(frozen=True)
class GetProductCommand:
    oid: UUID


@dataclass(frozen=True)
class GetProductListCommand:
    search: str | None = None
    sort: SortQueryParams = field(default_factory=SortQueryParams)
    pagination: PaginationQueryParams = field(default_factory=PaginationQueryParams)
