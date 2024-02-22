from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from category.models import ChildCategory
from carts.models import CartItem
from orders.models import OrderProduct
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.



def customkit(request, category_slug=None):
    categories = None
    products = None
    if category_slug is not None:
        categories = get_object_or_404(ChildCategory, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 8)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        # mostra apenas produtos disponiveis e os ordena pelo id
        products = Product.objects.all().filter(is_available=True).order_by("-id")
        paginator = Paginator(products, 16)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {"products": paged_products, "product_count": product_count}
    return render(request, "customkit/customkit.html", context)
