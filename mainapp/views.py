from django.shortcuts import render
from .models import Product
from cartapp.models import Cart

SHOP_NAME = 'BRAND'
STATIC_DATA = 'static/data/'

menu = [
    {'title': 'home', 'url': '/'},
    {'title': 'men', 'url': '#'},
    {'title': 'women', 'url': '#'},
    {'title': 'kids', 'url': '#'},
    {'title': 'accessories', 'url': '#'},
    {'title': 'featured', 'url': '#'},
    {'title': 'hot deals', 'url': '#'}
]


def main(request):
    title = 'home - ' + SHOP_NAME
    body_class = 'home'
    home_products = Product.objects.filter(category__pk=1).order_by('price')
    cart_amount = len(Cart.objects.all())
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'cart_amount': cart_amount,
        'products': home_products
    }
    return render(request, 'mainapp/index.html', content)


def checkout(request):
    title = 'checkout - ' + SHOP_NAME
    body_class = 'products'
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu
    }
    return render(request, 'mainapp/checkout.html', content)


def product(request):
    title = 'product - ' + SHOP_NAME
    body_class = 'products'
    products = Product.objects.filter(category__pk=2).order_by('price')
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': products
    }
    return render(request, 'mainapp/product.html', content)


# def cart(request):
#     title = 'shopping cart - ' + SHOP_NAME
#     body_class = 'products'
#     cart_products = Product.objects.filter(category__pk=4).order_by('price')
#     content = {
#         'title': title,
#         'body_class': body_class,
#         'menu': menu,
#         'products': cart_products
#     }
#     return render(request, 'mainapp/../cartapp/templates/cartapp/shopping-cart.html', content)


def single_page(request):
    title = 'single page - ' + SHOP_NAME
    body_class = 'single-page'
    page_products = Product.objects.filter(category__pk=3).order_by('price')
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': page_products
    }
    return render(request, 'mainapp/single-page.html', content)
