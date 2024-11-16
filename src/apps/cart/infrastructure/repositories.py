from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from src.apps.cart.infrastructure.models import CartItemDto


class ICartRepository(ABC):
    @abstractmethod
    def get_by_oid(self, oid: UUID) -> Optional[CartItemDto]:
        pass

    @abstractmethod
    def add_item(self, item: CartItemDto) -> CartItemDto:
        pass

    @abstractmethod
    def update_item(self, item: CartItemDto) -> CartItemDto:
        pass

    @abstractmethod
    def remove_item(self, item_oid: UUID) -> None:
        pass

    @abstractmethod
    def clear_item(self) -> None:
        pass


class PostgresCartRepository(ICartRepository):
    def get_by_oid(self, oid: UUID) -> Optional[CartItemDto]:
        return CartItemDto.objects.get(oid=oid)

    def add_item(self, item: CartItemDto) -> CartItemDto:
        return CartItemDto.objects.create(item=item)

    def update_item(self, item: CartItemDto) -> CartItemDto:
        return CartItemDto.objects.filter(oid=item.oid).update(qty=item.qty)

    def remove_item(self, item_oid: UUID) -> None:
        CartItemDto.objects.filter(oid=item_oid).delete()

    def clear_item(self) -> None:
        CartItemDto.objects.all().delete()
