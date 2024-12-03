from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app import models

# Register your models here.


@admin.register(models.User)
class CustomUser(UserAdmin):
    model = models.User

    fieldsets = UserAdmin.fieldsets + (
        (
            "Preferences",
            {
                "fields": (
                    "user_nickname",
                    "user_about",
                    "is_writter",
                )
            },
        ),
    )

    readonly_fields = ["user_id", "user_snowflake"]


admin.site.register(models.Tag)
admin.site.register(models.Post)
