from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("list-items", views.AllItemsView.as_view(), name="list-items"),
    path("list-items/<int:id>", views.ItemDetailView.as_view(), name="items-detail"),
]
