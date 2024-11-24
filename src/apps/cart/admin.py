from django.contrib import admin

from src.apps.cart.infrastructure.models import CartItemORM, CartORM

# Register your models here.


class CartItemInline(admin.TabularInline):
    model = CartItemORM


@admin.register(CartORM)
class CartORMAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = [
        "oid",
        "customer",
        "get_items",
        "is_active",
        "status",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["oid"]

    @admin.display(description="ITEMS")
    def get_items(self, obj: object):
        return "".join(f"{item.name}, cost: {item.cost}" for item in obj.items.all())
