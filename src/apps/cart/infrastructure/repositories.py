from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.cart.domain.entities import CartItem
from src.apps.cart.infrastructure.models import CartItemORM, CartORM
from src.apps.customer.infrastructure.models import CustomerORM


class ICartRepository(ABC):
    @abstractmethod
    def get_or_create_cart(self, customer_oid: UUID) -> CartORM:
        pass

    @abstractmethod
    def add_item(self, cart_oid: UUID, item: CartItem) -> CartItemORM:
        pass

    @abstractmethod
    def update_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItemORM:
        pass

    @abstractmethod
    def remove_item(self, item: CartItem) -> CartItemORM:
        pass

    @abstractmethod
    def clear_items(self, cart_oid: UUID) -> list[CartItemORM]:
        pass

    @abstractmethod
    def increase_item_quantity(self, item: CartItem) -> CartItemORM:
        pass


class PostgresCartRepository(ICartRepository):
    def get_or_create_cart(self, customer_oid: UUID) -> CartORM:
        customer_orm = CustomerORM.objects.get(oid=customer_oid)
        cart_orm, _ = CartORM.objects.get_or_create(customer=customer_orm)
        return cart_orm

    def add_item(self, cart_oid: UUID, item: CartItem) -> CartItemORM:
        cart_orm = CartORM.objects.get(oid=cart_oid)
        cart_item_orm = CartItemORM.objects.create(
            cart=cart_orm, product=item.product, quantity=item.quantity, cost=item.cost
        )
        return cart_item_orm

    def update_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItemORM:
        cart_item_orm = CartItemORM.objects.get(cart__oid=cart_oid, oid=item_oid)
        cart_item_orm.quantity += quantity
        cart_item_orm.save(update_fields=["quantity"])
        return cart_item_orm

    def remove_item(self, cart_oid: UUID, item_oid: UUID) -> CartItemORM:
        cart_item_orm = CartItemORM.objects.get(cart__oid=cart_oid, item_oid=item_oid)
        CartItemORM.objects.filter(cart__oid=cart_oid, oid=item_oid).delete()
        return cart_item_orm

    def clear_items(self, cart_oid: UUID) -> list[CartItemORM]:
        cart = CartORM.objects.get(oid=cart_oid)
        items = cart.cart_items.all()
        cart.cart_items.all().delete()
        return list(items)
