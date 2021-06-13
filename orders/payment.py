import requests
import json

def pay_with_flutterwave(amount, email, name, store_name, reference):
    base_url = 'https://api.flutterwave.com/v3/payments'

    public_key = 'FLWPUBK_TEST-aaab004122d871bc5c7ea7ade0048fd9-X'

    secret_key = 'FLWSECK_TEST-6780cf75dc1d85b632abee0f01420b9a-X'

    # tx_ref = '123454'

    headers = {'Authorization': f"Bearer {secret_key}"}

    payload = {"tx_ref": reference,
            "amount": str(amount),
            "currency": "NGN",
            "redirect_url": "https://google.com",
            "payment_options": "card",
            "customer":{
                "email": email,
                "phonenumber": "08103087162",
                "name": name,
            },
            "customizations":{
            "title":store_name,
            "description":"Middleout isn't free. Pay the price",
            "logo":"https://assets.piedpiper.com/logo.png"
       }
    }

    response = requests.post(base_url, json=payload, headers=headers).json()
    return {'response': response}

# 5531 8866 5214 2950

# 564

# 09/32
# 3310
# 12345