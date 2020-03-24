from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from checkout.models import OrderLineItem
from django.contrib import messages     

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    print(request.user.is_authenticated)
    print(request.user.email)
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a photo to the cart"""
    cart = request.session.get('cart', {})
    if id in cart:
        messages.error(request, "Item is already in cart!")
        print(messages)
    else:
        cart[id] = cart.get(id)
    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('view_cart'))

def remove_from_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount.
    """
    cart = request.session.get('cart', {})
    cart.pop(id)
    print(cart)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))