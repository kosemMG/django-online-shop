from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from cartapp.models import Cart
from mainapp.models import Product


def view_cart(request):
    title = 'cart - Brand'
    products = []
    cart_products = Cart.objects.filter(user=request.user)

    for i, cart_product in enumerate(cart_products):
        products.append(Product.objects.get(pk=cart_product.product_id))

    cart_amount = len(products)
    content = {
        'title': title,
        'products': products,
        'cart_amount': cart_amount
    }
    return render(request, 'cartapp/shopping-cart.html', content)


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart.objects.filter(user=request.user, product=product).first()

    if not cart:
        cart = Cart(user=request.user, product=product)

    cart.amount += 1
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request):
    content = {}
    return render(request, 'cartapp/shopping-cart.html', content)
