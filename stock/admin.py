from django.contrib import admin
from .models import Item, Warehouse


class ItemAdmin(admin.ModelAdmin):
    list_display = ("state", "category", "warehouse")


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Item, ItemAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
