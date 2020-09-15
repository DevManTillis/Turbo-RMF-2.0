from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.AccountProfile)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "username", "is_active"]

    class Meta:
        model = models.AccountProfile