import requests
import json
from rest_framework.exceptions import APIException


def create_subaccount(account_bank, account_number, business_name):
    try:
        url = 'https://api.flutterwave.com/v3/subaccounts'

        secret_key = 'FLWSECK_TEST-6780cf75dc1d85b632abee0f01420b9a-X'

        headers = {'Authorization': f"Bearer {secret_key}"}

        payload = {
            "account_bank": account_bank,
            "account_number": account_number,
            "business_name": business_name,
            "business_email": "petya@stux.net",
            "business_contact": "Anonymous",
            "business_contact_mobile": "090890382",
            "business_mobile": "09087930450",
            "country": "NG",
            "split_type": "percentage",
            "split_value": 0.05
        }
        subaccount = requests.post(url, json=payload, headers=headers).json()
    except:
        return {'error': 'Your store cannot be created at this moment, please try again!!!'}
    return {'result': subaccount}


class BadRequestToFlutterwave(APIException):
    status_code = 400
    default_detail = "Unable to create store, please ensure your account details are corrrect!!!"
    default_code = "error"