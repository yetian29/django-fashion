from dataclasses import dataclass
from uuid import UUID

from apps.base.domain.error import DomainValidationError
from apps.base.domain.value_objects import ValueObject


@dataclass(frozen=True)
class ProductId(ValueObject):
    value: UUID


@dataclass(frozen=True)
class ProductName(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Invalid. Product name is required.")
        elif len(self.value) > 64:
            raise DomainValidationError(
                "Invalid. Product name has to less than or equal 64 character."
            )


@dataclass(frozen=True)
class ProductPrice(ValueObject):
    value: int

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Invalid. Product price is required.")
        elif self.value < 0:
            raise DomainValidationError("Invalid. Product price has to be positive.")


@dataclass(frozen=True)
class ProductDescription(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise DomainValidationError("Invalid. Product description is required.")
        elif self.value > 1024:
            raise DomainValidationError(
                "Invalid. Product description has to less than or equal 1024 character."
            )
