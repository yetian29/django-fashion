from django.contrib import admin

from src.apps.cart.infrastructure.models import CartDto

# Register your models here.


class CartDtoAdmin(admin.ModelAdmin):
    list_display = ["oid", "items", "is_active", "created_at", "updated_at"]
    list_display_links = ["oid"]


admin.site.register(CartDto, CartDtoAdmin)
