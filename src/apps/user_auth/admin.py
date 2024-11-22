from django.contrib import admin

from src.apps.user_auth.infrastructure.models import UserAuthORM

# Register your models here.


@admin.register(UserAuthORM)
class UserAuthORMAdmin(admin.ModelAdmin):
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
