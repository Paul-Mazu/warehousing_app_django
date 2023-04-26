from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Item, Warehouse, Employee
from django.db.models import Count, Min, Value
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models.functions import Concat


cart = []


def index(request):
    return render(request, "stock/index.html")


class AllItemsView(ListView):
    template_name = "stock/list-items.html"
    model = Item
    context_object_name = "items"

    def get_queryset(self):

        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.annotate(
                state_and_category=Concat('state', Value(' '), 'category')
            ).filter(state_and_category__icontains=query)

        items = queryset.values('state', 'category') \
            .annotate(num_items=Count('id'), id=Min('id')) \
            .order_by('state', 'category')

        return items


class ItemDetailView(View):

    def get(self, request, id):
        item = Item.objects.get(pk=id)
        items = Item.objects.filter(
            state=item.state, category=item.category).order_by('date_of_stock')
        return render(request, "stock/item-detail.html", {
            "items": items,
            "cart": cart
        })
    
def add_to_cart(request, id):
    item = Item.objects.get(id = id)
    cart.append(item)
    return HttpResponseRedirect(reverse("items-detail", args=[id]))


def remove_from_cart(request, id):
    item = Item.objects.get(id = id)
    cart.remove(item)
    return HttpResponseRedirect(reverse("cart"))


def cart_view(request):
    return render(request, "stock/cart.html", {"items": cart})


def place_order(request):
    pass