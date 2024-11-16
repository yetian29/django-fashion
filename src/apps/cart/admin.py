from django.contrib import admin

from src.apps.cart.infrastructure.models import CartDto

# Register your models here.


class CartDtoAdmin(admin.ModelAdmin):
    list_display = ["oid", "get_items", "created_at", "updated_at", "is_active"]
    list_display_links = ["oid"]
    filter_horizontal = ["items"]

    def get_items(self, obj: object) -> str:
        return ", ".join([str(item) for item in obj.items.all()])

    get_items.short_description = "items"  # Column Header in admin


admin.site.register(CartDto, CartDtoAdmin)
