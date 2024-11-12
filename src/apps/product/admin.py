from django.contrib import admin

from apps.product.domain.entities import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "description"]


admin.register(Product, ProductAdmin)
