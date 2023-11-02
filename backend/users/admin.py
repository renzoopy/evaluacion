from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "full_name",
        "is_approved",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = ("id", "email")
    ordering = ("id",)

    def full_name(self, obj):
        return f"{obj.full_name}"

    full_name.short_description = "Full name"
