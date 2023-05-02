from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("state", "category", "warehouse")


admin.site.register(Item, ItemAdmin)

# Register your models here.
