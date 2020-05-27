from django.shortcuts import render, get_object_or_404
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

    cart = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)

    products = []
    for cart_product in cart:
        product = Product.objects.get(pk=cart_product.product_id)
        products.append({
            'product': product,
            'number': cart_product.amount,
            'subtotal': product.price * cart_product.amount
        })

    cart_amount = len(products)

    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'cart_amount': cart_amount,
        'products': home_products,
        'cart_products': products,
        'cart': cart
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

    cart = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)

    cart_products = []
    for cart_product in cart:
        product = Product.objects.get(pk=cart_product.product_id)
        cart_products.append({
            'product': product,
            'number': cart_product.amount,
            'subtotal': product.price * cart_product.amount
        })

    cart_amount = len(cart_products)

    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'cart_amount': cart_amount,
        'products': products,
        'cart_products': cart_products,
        'cart': cart
    }
    return render(request, 'mainapp/product.html', content)


def single_page(request, pk):
    title = 'single page - ' + SHOP_NAME
    body_class = 'single-page'
    single_product = get_object_or_404(Product, pk=pk)
    page_products = Product.objects.filter(category__pk=3).order_by('price')

    cart = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)

    products = []
    for cart_product in cart:
        product = Product.objects.get(pk=cart_product.product_id)
        products.append({
            'product': product,
            'number': cart_product.amount,
            'subtotal': product.price * cart_product.amount
        })

    cart_amount = len(products)

    content = {
        'title': title,
        'body_class': body_class,
        'menu': menu,
        'cart_amount': cart_amount,
        'product': single_product,
        'products': page_products,
        'cart_products': products,
        'cart': cart
    }
    return render(request, 'mainapp/single-page.html', content)
