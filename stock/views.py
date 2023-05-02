from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Item, Warehouse, Employee
from django.db.models import Count, Min, Value
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models.functions import Concat
from django.urls import resolve


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

        if not request.session.get('cart'):
            request.session['cart'] = []

        return render(request, "stock/item-detail.html", {
            "items": items,
            "cart": request.session['cart']
        })


def add_to_cart(request, id):
    cart = request.session['cart']
    cart.append(id)
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse("stock:items-detail", args=[id]))


def remove_from_cart(request, id):
    cart = request.session.get("cart")
    cart.remove(id)
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse("stock:cart"))


def cart_view(request):
    items = []
    list_ids = request.session.get('cart')
    if list_ids:
        items = [Item.objects.get(id=id) for id in list_ids]
    return render(request, "stock/cart.html", {"items": items})


def place_order(request):
    cart = request.session.get("cart")
    empty_cart = True

    if cart:
        empty_cart = False
        Item.objects.filter(id__in=cart).delete()
    
    return render(request, "stock/order-placed.html", context= {
            "empty_cart" : empty_cart
        })
   
    

def remove_order(request):
    request.session["cart"] = []
    next_url = request.GET.get('next')
    return HttpResponseRedirect(next_url)
    
