from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class ValueObject:
    pass


class SortOrderEnum(int, Enum):
    asc = 1
    desc = -1


@dataclass(frozen=True)
class SortQuery(ValueObject):
    sort_field: str = "oid"
    sort_order: SortOrderEnum = SortOrderEnum.asc


@dataclass(frozen=True)
class PaginationQuery(ValueObject):
    page: int = 0
    limit: int = 20

    @property
    def offset(self) -> int:
        return self.page * self.limit
