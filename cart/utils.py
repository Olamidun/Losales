import json
from accounts.models import Customer
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
        customer.save()
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
        print(items)
        cart_count = order.get_order_items
    else:
        data = cookie_cart(request)
        cart_count = data['cart_count']
        items = data['items']
        order = data['order']
    return {'items':items, 'order': order, 'cart_count': cart_count}


# def create_subaccount():
#     base_url = 'https://api.flutterwave.com/v3/subaccounts'
#     public_key = 'FLWPUBK_TEST-aaab004122d871bc5c7ea7ade0048fd9-X'

#     secret_key = 'FLWSECK_TEST-6780cf75dc1d85b632abee0f01420b9a-X'

#     headers = {'Authorization': f"Bearer {secret_key}"}
#     payload = {
#         "account_bank": "044",
#         "account_number": "0690000037",
#         "business_name": "Eternal Blue",
#         "business_email": "petya@stux.net",
#         "business_contact": "Anonymous",
#         "business_contact_mobile": "090890382",
#         "business_mobile": "09087930450",
#         "country": "NG",
#         "split_type": "percentage",
#         "split_value": 0.5
#     }

#     response = requests.post(base_url, json=payload, headers)

#     print(response)