from dataclasses import dataclass
from enum import Enum

from src.apps.base.helper.errors import fail
from src.apps.cart.domain.errors import QtyInvalidException


@dataclass(frozen=True)
class ValueObject:
    pass


@dataclass(frozen=True)
class Qty(ValueObject):
    value: int

    def __post_init__(self) -> None:
        if not self.value or self.value < 0 or self.value > 10:
            fail(QtyInvalidException)


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
