import requests
import json


def create_subaccount(account_bank, account_number):
    url = 'https://api.flutterwave.com/v3/subaccounts'

    secret_key = 'FLWSECK_TEST-6780cf75dc1d85b632abee0f01420b9a-X'

    headers = {'Authorization': f"Bearer {secret_key}"}

    payload = {
        "account_bank": account_bank,
        "account_number": account_number,
        "business_name": "Eternal Blue",
        "business_email": "petya@stux.net",
        "business_contact": "Anonymous",
        "business_contact_mobile": "090890382",
        "business_mobile": "09087930450",
        "country": "NG",
        "split_type": "percentage",
        "split_value": 0.05
    }
    subaccount = requests.post(url, json=payload, headers=headers).json()
    return {'result': subaccount}