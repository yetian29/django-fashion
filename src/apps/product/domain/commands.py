from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from src.apps.base.domain.value_objects import PaginationQuery, SortQuery


@dataclass(frozen=True)
class GetProductCommand:
    oid: UUID


@dataclass(frozen=True)
class GetProductListCommand:
    search: Optional[str] = None
    sort: SortQuery = field(default_factory=SortQuery)
    pagination: PaginationQuery = field(default_factory=PaginationQuery)
