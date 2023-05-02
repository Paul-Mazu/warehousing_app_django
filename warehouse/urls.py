from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("stock/", include("stock.urls", namespace="stock")),
    path("account/", include("account.urls", namespace="account")),
]
