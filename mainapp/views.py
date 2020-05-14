from django.shortcuts import render
from json import load

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
    products = get_data_from_json(STATIC_DATA + 'home_products.json')
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': products
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
    products = get_data_from_json(STATIC_DATA + 'products.json')
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
    products = get_data_from_json(STATIC_DATA + 'cart_products.json')
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': products
    }
    return render(request, 'mainapp/shopping-cart.html', content)


def single_page(request):
    title = 'single page - ' + SHOP_NAME
    body_class = 'single-page'
    products = get_data_from_json(STATIC_DATA + 'page_products.json')
    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'products': products
    }
    return render(request, 'mainapp/single-page.html', content)
