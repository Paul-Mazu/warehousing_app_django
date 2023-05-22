from rest_framework import generics
from .models import Item, Warehouse
from .serializers import ItemSerializer, WarehouseSerializer
from rest_framework.permissions import IsAuthenticated


class ItemApiListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [
        IsAuthenticated,
    ]


class ItemApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"
    permission_classes = [
        IsAuthenticated,
    ]
