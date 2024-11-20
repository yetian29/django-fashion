from django.contrib import admin

from src.apps.cart.infrastructure.models import CartItemORM, CartORM

# Register your models here.


@admin.register(CartItemORM)
class CartItemORMAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity"]


@admin.register(CartORM)
class CartORMAdmin(admin.ModelAdmin):
    list_display = [
        "oid",
        "items",
        "is_active",
        "status",
        "total_count",
        "total_price",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["oid"]
