from django.contrib import admin

from src.apps.cart.infrastructure.models import CartDto
from src.apps.product.infrastructure.models import ProductDto

# Register your models here.


class ProductDtoInline(admin.TabularInline):
    model = ProductDto


class CartDtoAdmin(admin.ModelAdmin):
    list_display = ["oid", "get_products", "is_active", "created_at", "updated_at"]
    list_display_links = ["oid"]

    def get_products(self, obj: object) -> str:
        return ", ".join([str(product) for product in obj.products.all()])

    get_products.short_description = "products"  # Column Header in admin


admin.site.register(CartDto, CartDtoAdmin)
