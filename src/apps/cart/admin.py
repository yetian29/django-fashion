from django.contrib import admin

from src.apps.cart.infrastructure.models import CartItemORM, CartORM

# Register your models here.


class CartItemORMInline(admin.TabularInline):
    model = CartItemORM
    fk_name = "cart"


@admin.register(CartORM)
class CartORMAdmin(admin.ModelAdmin):
    inlines = [CartItemORMInline]
    list_display = [
        "oid",
        "is_active",
        "status",
        "total_count",
        "total_price",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["oid"]
