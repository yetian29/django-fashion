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
        "items",
        "status",
        "total_count",
        "total_price",
        "created_at",
        "updated_at",
        "is_active",
    ]
    list_display_links = ["oid"]

    @admin.display(description="ITEMS")
    def items(self, obj: object) -> str:
        return ", ".join(
            f"{item.product.name} (qty: {item.quantity}) (price: {item.product.price})"
            for item in obj.items.all()
        )
