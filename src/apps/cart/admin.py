from django.contrib import admin

from src.apps.cart.infrastructure.models import CartItemORM, CartORM


# Register your models here.
class CartItemORMInline(admin.TabularInline):
    model = CartItemORM


@admin.register(CartORM)
class CartORMAdmin(admin.ModelAdmin):
    inlines = [CartItemORMInline]
    list_display = ["oid", "items", "is_active", "status", "created_at", "udpated_at"]
    list_display_links = ["oid"]
