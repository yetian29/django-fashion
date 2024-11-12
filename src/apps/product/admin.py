from django.contrib import admin

from src.apps.product.infrastructure.models import ProductDto

# Register your models here.


class ProductDtoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "description"]


admin.register(ProductDto, ProductDtoAdmin)
