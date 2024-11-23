from django.contrib import admin

from src.apps.customer.infrastructure.models import CustomerORM

# Register your models here.


@admin.register(CustomerORM)
class CustomerORMAdmin(admin.ModelAdmin):
    list_display = [
        "oid",
        "phone_number",
        "email",
        "token",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["oid", "phone_number", "email"]
    search_fields = ["phone_number", "email"]
