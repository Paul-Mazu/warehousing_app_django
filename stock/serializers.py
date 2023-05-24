from rest_framework import serializers
from .models import Item, Warehouse


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "state",
            "category",
            "date_of_stock",
            "warehouse",
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            "name",
        ]
