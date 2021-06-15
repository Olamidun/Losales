import requests
import json

def pay_with_flutterwave(amount, email, name, store_name, reference, subaccount_id):
    base_url = 'https://api.flutterwave.com/v3/payments'

    # public_key = 'FLWPUBK_TEST-YYYYYYYYYYYYYYYYYYYY'

    secret_key = 'FLWSECK_TEST-XXXXXXXXXXXXXX'

    # tx_ref = '123454'

    headers = {'Authorization': f"Bearer {secret_key}"}

    payload = {"tx_ref": reference,
            "amount": str(amount),
            "currency": "NGN",
            "redirect_url": "http://localhost:8000/store/eternal-blue/orders/52/confirm_payment",
            "payment_options": "card",
            "customer":{
                "email": email,
                "phonenumber": "08103087162",
                "name": name,
            },
            "subaccounts": [
                {
                    "id": subaccount_id
                },
            ],
            "customizations":{
            "title":store_name,
            "description":"Middleout isn't free. Pay the price",
            "logo":"https://assets.piedpiper.com/logo.png"
       }
    }

    response = requests.post(base_url, json=payload, headers=headers).json()
    return {'response': response}


def confirm_payment(transaction_id):
    secret_key = 'FLWSECK_TEST-XXXXXXXXXXXX'

    headers = {"Content-Type": 'application/json', 'Authorization': f"Bearer {secret_key}"}

    base_url = f'https://api.flutterwave.com/v3/transactions/{transaction_id}/verify'

    response = requests.get(base_url, headers=headers).json()
    return {'response': response}
    

# 5531 8866 5214 2950

# 564

# 09/32
# 3310
# 12345