from django.contrib import admin

from src.apps.product.infrastructure.models import ProductDto

# Register your models here.


class ProductDtoAdmin(admin.ModelAdmin):
    list_display = ["oid", "name", "description", "price", "created_at", "updated_at"]
    list_display_links = ["oid", "name"]
    search_fields = ["name", "description"]


admin.site.register(ProductDto, ProductDtoAdmin)
