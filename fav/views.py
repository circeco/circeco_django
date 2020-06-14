from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_fav(request):
    """A View that renders the cart contents page"""
    return render(request, "fav.html")


def add_to_fav(request, shopId):
    """xxx"""

    userId = request.user
    # TODO associate userId and shopId

    print(shopId, userId)

    return redirect(reverse('index'))


def remove_fav(request, shopId):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))