from django.urls import path
from . import views, views_api

app_name = "stock"

urlpatterns = [
    path("", views.index, name="index-page"),
    path("list-items", views.AllItemsView.as_view(), name="list-items"),
    path("list-items/<int:id>/", views.ItemDetailView.as_view(), name="items-detail"),
    path("add-to-cart/<int:id>", views.add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<int:id>", views.remove_from_cart, name="remove-from-cart"),
    path("cart", views.cart_view, name="cart"),
    path("place-order", views.place_order, name="place-order"),
    path("remove-order", views.remove_order, name="remove-order"),
    # APIs
    path("api/list-items/", views_api.ItemApiListView.as_view(), name="api-list-item"),
    path(
        "api/list-items/<int:id>/",
        views_api.ItemApiDetailView.as_view(),
        name="api-items-detail",
    ),
]
