from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, reverse
from django.contrib.auth.decorators import login_required

from cartapp.models import Cart
from mainapp.models import Product


@login_required
def view_cart(request):
    title = 'cart - Brand'

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
        'cart_products': products,
        'cart_amount': cart_amount,
        'cart': cart
    }
    return render(request, 'cartapp/shopping-cart.html', content)


@login_required
def add_to_cart(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('single_page', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    cart = Cart.objects.filter(user=request.user, product=product).first()

    if not cart:
        cart = Cart(user=request.user, product=product)

    cart.amount += 1
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_cart(request, product_id):
    card_record = Cart.objects.filter(product__pk=product_id)
    card_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
