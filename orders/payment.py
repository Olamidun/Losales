import requests
import json

class Flutterwave:
    def __init__(self, secret_key):
        self.secret_key = secret_key


    def __authentication_headers(self):
        headers = {"Content-Type": 'application/json', "Authorization": f"Bearer {self.secret_key}"}
        return headers

    def pay_with_flutterwave(self, amount, email, name, store_name, reference, subaccount_id, order_id):
        base_url = 'https://api.flutterwave.com/v3/payments'

        # tx_ref = '123454'

        headers = self.__authentication_headers()

        payload = {"tx_ref": reference,
                "amount": str(amount),
                "currency": "NGN",
                "redirect_url": f"http://localhost:8000/store/{store_name}/orders/{order_id}/confirm_payment",
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


    def confirm_payment(self, transaction_id):

        headers = self.__authentication_headers()

        base_url = f'https://api.flutterwave.com/v3/transactions/{transaction_id}/verify'

        response = requests.get(base_url, headers=headers).json()
        return {'response': response}

    

# 5531 8866 5214 2950

# 564

# 09/32
# 3310
# 12345