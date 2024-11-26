import json
from abc import ABC, abstractmethod
from uuid import UUID

import redis
from django.db import transaction

from src.apps.cart.domain.entities import CartItem
from src.apps.cart.infrastructure.models import CartItemORM, CartORM
from src.apps.customer.infrastructure.models import CustomerORM
from src.apps.product.infrastructure.models import ProductORM


class ICartRepository(ABC):
    @abstractmethod
    def get_or_create_cart(self, customer_oid: UUID) -> CartORM:
        pass

    @abstractmethod
    @transaction.atomic
    def add_item(self, cart_oid: UUID, item: CartItem) -> CartItemORM:
        pass

    @abstractmethod
    @transaction.atomic
    def update_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItemORM:
        pass

    @abstractmethod
    @transaction.atomic
    def remove_item(self, cart_oid: UUID, item_oid: UUID) -> CartItemORM:
        pass

    @abstractmethod
    @transaction.atomic
    def clear_items(self, cart_oid: UUID) -> list[CartItemORM]:
        pass

    @abstractmethod
    @transaction.atomic
    def increase_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItemORM:
        pass


class MixinCartRepository(ICartRepository):
    def __init__(self, redis_client: redis.Redis) -> None:
        self.redis = redis_client

    def _generate_cart_key(self, customer_oid: UUID) -> str:
        return f"customer_cart: {customer_oid}"

    def _generate_cart_items_key(self, cart_oid: UUID) -> str:
        return f"cart_item: {cart_oid}"

    def _serialize_cart_item(self, item: CartItem) -> str:
        return json.dumps(
            {
                "oid": str(item.oid),
                "cart_oid": str(item.cart_oid),
                "product_oid": str(item.product.oid),
                "product_name": item.product.name,
                "quantity": item.quantity,
                "price": item.product.price,
                "cost": item.cost,
            }
        )

    def _deserialize_cart_item(self, serialize: str) -> CartItem:
        item_data = json.loads(serialize)
        product = ProductORM.objects.get(oid=UUID(item_data["product_oid"]))

        return CartItem(
            oid=item_data["oid"],
            cart_oid=item_data["cart_oid"],
            product=product,
            quantity=item_data["quantity"],
            cost=item_data["cost"],
        )

    def get_or_create_cart(self, customer_oid: UUID) -> CartORM:
        customer_orm = CustomerORM.objects.get(oid=customer_oid)
        cart_key = self._generate_cart_key(customer_oid=customer_orm.oid)
        cached_cart = self.redis.get(cart_key)
        if cached_cart:
            return CartORM.objects.get(customer=customer_orm)

        # Create or Get Cart from Postgresql
        cart_orm, _ = CartORM.objects.get_or_create(
            customer__oid=customer_oid, defaults={"is_active": True}
        )
        self.redis.setex(cart_key, 3600, str(cart_orm.oid))
        return cart_orm

    @transaction.atomic
    def add_item(self, cart_oid: UUID, item: CartItem) -> CartItemORM:
        cart_orm = CartORM.objects.get(oid=cart_oid)
        # Kiểm tra số lượng items trong cart
        if cart_orm.items.count() >= cart_orm.MAX_CONTAINER:
            raise ValueError("Giỏ hàng đã đạt giới hạn số lượng sản phẩm")
        cart_item_orm = CartItemORM.objects.create(
            cart=cart_orm, product=item.product, quantity=item.quantity, cost=item.cost
        )
        cart_items_key = self._generate_cart_items_key(cart_oid)
        self.redis.hset(
            cart_items_key, str(cart_item_orm.oid), self._serialize_cart_item(item)
        )

        # Đặt timeout cho các items
        self.redis.expire(cart_items_key, 3600)

        # Cập nhật trạng thái giỏ hàng
        cart_orm.update_status()
        cart_orm.save()

        return cart_item_orm

    @transaction.atomic
    def update_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItemORM:
        cart_item_orm = CartItemORM.objects.get(cart__oid=cart_oid, oid=item_oid)
        cart_item_orm.quantity += quantity
        cart_item_orm.save(update_fields=["quantity"])
        # Cập nhật trong Redis
        cart_items_key = self._generate_cart_items_key(cart_oid)
        # Lấy item từ Redis và cập nhật
        existing_item = self.redis.hget(cart_items_key, str(item_oid))
        if existing_item:
            item_data = self._deserialize_cart_item(existing_item)
            item_data["quantity"] += quantity
            self.redis.hset(cart_items_key, str(item_oid), json.dumps(item_data))
        return cart_item_orm

    @transaction.atomic
    def remove_item(self, cart_oid: UUID, item_oid: UUID) -> CartItemORM:
        cart_item_orm = CartItemORM.objects.get(cart__oid=cart_oid, oid=item_oid)
        # xóa item trong PostgresSQL
        cart_item_orm.delete()

        # Xóa khỏi Redis
        cart_items_key = self._generate_cart_items_key(cart_oid)
        self.redis.hdel(cart_items_key, str(item_oid))
        return cart_item_orm

    @transaction.atomic
    def clear_items(self, cart_oid: UUID) -> list[CartItemORM]:
        cart_items = CartItemORM.objects.filter(cart__oid=cart_oid)
        # Xóa tất cả items trong PostgreSQL
        cart_items.delete()
        # Xóa khỏi Redis
        cart_items_key = self._generate_cart_items_key(cart_oid)
        self.redis.delete(cart_items_key)
        return list(cart_items)

    @transaction.atomic
    def increase_item_quantity(
        self, cart_oid: UUID, item_oid: UUID, quantity: int
    ) -> CartItemORM:
        cart_item_orm = CartItemORM.objects.get(cart__oid=cart_oid, oid=item_oid)
        cart_item_orm.quantity = quantity
        cart_item_orm.save(update_fields=["quantity"])
        # Cập nhật trong Redis
        cart_items_key = self._generate_cart_items_key(cart_oid)

        existing_item = self.redis.hget(cart_items_key, str(item_oid))
        if existing_item:
            item_data = self._deserialize_cart_item(existing_item)
            item_data["quantity"] = quantity

            self.redis.hset(
                cart_items_key, str(item_oid), self._serialize_cart_item(item_data)
            )
        return cart_item_orm
