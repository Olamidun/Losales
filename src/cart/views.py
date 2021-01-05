from django.shortcuts import render
from .models import Order, OrderItem, ShippingAddress

# Create your views here.


def cart(request):
    context = {}
    return render('cart/cart.html', context)

def checkout(request):
    context = {}
    return render('cart/cart.html', context)

'''
    def cart(request):
        context = {}
        return render('cart/cart.html', context)
'''
