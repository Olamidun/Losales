import json
from store.models import Product
from .models import Order, OrderItem, ShippingAddress
from django.http import JsonResponse


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
        # print(cart)
    except:
        cart = {}
    items = []
    order = {'get_order_total': 0, 'get_order_items': 0}
    cart_count = order['get_order_items']

    for i in cart:
        print(i)
        try:
            cart_count += cart[i]['quantity']
            product = Product.objects.get(id=i)
            print(product)
            total = product.price * cart[i]['quantity']
            order['get_order_total'] +=  total
            order['get_order_items'] += cart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name_of_product,
                    'price': product.price,
                    'image_url': product.image_url,
                    },
                'quantity': cart[i]['quantity'],
                'get_total': total    
            }

            items.append(item)
            print(items)
            
        except:
            pass
    return {'items':items, 'order': order, 'cart_count': cart_count}


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_count = order.get_order_items
    else:
        data = cookie_cart(request)
        cart_count = data['cart_count']
        items = data['items']
        order = data['order']
    return {'items':items, 'order': order, 'cart_count': cart_count}