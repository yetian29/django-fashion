from django.contrib import admin

from src.apps.product.infrastructure.models import ProductORM

# Register your models here.


@admin.register(ProductORM)
class ProductORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name", "description", "price", "created_at", "updated_at"]
    list_display_links = ["oid", "name"]
