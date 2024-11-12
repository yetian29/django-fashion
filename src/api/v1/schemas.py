from typing import Any, Generic, TypeVar

from ninja import Field, Schema

TData = TypeVar("TData")


class ApiResponse(Schema, Generic[TData]):
    data: TData | list | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    error: list[Any] = Field(default_factory=list)
