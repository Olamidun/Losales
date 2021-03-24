import random
import string
import json
import requests
from .models import Store


public_key = 'FLWPUBK_TEST-aaab004122d871bc5c7ea7ade0048fd9-X'

secret_key = 'FLWSECK_TEST-6780cf75dc1d85b632abee0f01420b9a-X'


base_url = 'https://api.flutterwave.com/v3/'



def pay(request, slug):
    payment_url = f'{base_url}/v3/payments'
    store = Store.objects.get(owner=request.user, slug=slug, is_approved=False)
    print(store)
    rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])

    tx_ref = rand

    headers = {'Authorization': f"Bearer {secret_key}"}

    payload = {
        "tx_ref": tx_ref,
        "amount": "100",
        "currency": "NGN",
        "redirect_url": f"http://localhost:8000/confirm_payment/{store.slug}",
        "payment_options": "card",
        "customer":{
            "email": f"{store.owner.email}",
            "phonenumber": "08103087162",
            "name": f"{store.owner.first_name} {store.owner.last_name}",
        },
        "customizations":{
        "title":"Pied Piper Payments",
        "description":"Middleout isn't free. Pay the price",
        "logo":"https://assets.piedpiper.com/logo.png"}
    }

    store.reference = tx_ref
    store.save()
    print(store.slug)

    response = requests.post(base_url, json=payload, headers=headers)
    results = response.json()

    json_result = json.loads(results)

    redirect_link = json_result['data']['link']
    return {'redirect_link': redirect_link}