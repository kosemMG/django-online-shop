from django.shortcuts import render
from django.conf import settings
from json import load
from .models import ProductCategory, Product

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


def get_data_from_json(src: str):
    with open(src) as file:
        return load(file)


def main(request):
    title = 'home - ' + SHOP_NAME
    body_class = 'home'
    home_products = Product.objects.filter(category_id=1)
    # products = get_data_from_json(STATIC_DATA + 'home_products.json')
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
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
    # products = get_data_from_json(STATIC_DATA + 'products.json')
    products = Product.objects.filter(category_id=2)
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': products
    }
    return render(request, 'mainapp/product.html', content)


def cart(request):
    title = 'shopping cart - ' + SHOP_NAME
    body_class = 'products'
    # products = get_data_from_json(STATIC_DATA + 'cart_products.json')
    cart_products = Product.objects.filter(category_id=4)
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': cart_products
    }
    return render(request, 'mainapp/shopping-cart.html', content)


def single_page(request):
    title = 'single page - ' + SHOP_NAME
    body_class = 'single-page'
    # products = get_data_from_json(STATIC_DATA + 'page_products.json')
    page_products = Product.objects.filter(category_id=3)
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': page_products
    }
    return render(request, 'mainapp/single-page.html', content)
