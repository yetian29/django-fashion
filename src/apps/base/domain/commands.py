from dataclasses import dataclass, field
from enum import Enum


class SortOrderEnum(int, Enum):
    asc = 1
    desc = -1


@dataclass(frozen=True)
class SortQueryParams:
    sort_field: str = "oid"
    sort_order: SortOrderEnum = field(default_factory=SortOrderEnum)


@dataclass(frozen=True)
class PaginationQueryParams:
    page: int = 0
    limit: int = 20

    @property
    def offset(self) -> int:
        return self.page * self.limit
