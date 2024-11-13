from django.contrib import admin

from src.apps.cart.infrastructure.models import CartDto

# Register your models here.


class CartDtoAdmin(admin.ModelAdmin):
    list_display = ["oid", "get_products", "created_at", "updated_at", "is_active"]
    list_display_links = ["oid"]
    filter_horizontal = ["products"]

    def get_products(self, obj: object) -> str:
        return ", ".join([str(product) for product in obj.products.all()])

    get_products.short_description = "products"  # Column Header in admin


admin.site.register(CartDto, CartDtoAdmin)
