import json
from django.shortcuts import render
from store.models import Product
from .models import Order, OrderItem, ShippingAddress
from django.http import JsonResponse

# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_count = order.get_order_items
    else:
        items = []
        order = {'get_order_total': 0, 'get_order_items': 0}
        cart_count = order['get_order_items']
    context = {'items':items, 'order': order, 'cart_count': cart_count}
    return render(request, 'cart/cart.html', context)

def update_item(request):
    # get the response from the fetch request in cart.js and turn it into a dictionary
    data = json.loads(request.body)

    product_id = data['productId']
    action = data['action']
    print(product_id, action)

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity += 1
    elif action == 'remove':
        orderitem.quantity -= 1
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse('Item added', safe=False)


def checkout(request):
    context = {}
    return render('cart/cart.html', context)

'''
    def cart(request):
        context = {}
        return render('cart/cart.html', context)
'''
