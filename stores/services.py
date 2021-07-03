import requests
import redis
import json
from rest_framework.exceptions import APIException
import os
from dotenv import load_dotenv

load_dotenv()

class SubaccountClass:
    def __init__(self, secret_key):
        self.secret_key = secret_key


    def __authentication_headers(self):
        headers = {"Content-Type": 'application/json', "Authorization": f"Bearer {self.secret_key}"}
        return headers


    def create_subaccount(self, account_bank, account_number, business_name, ):
        
        try:
            url = 'https://api.flutterwave.com/v3/subaccounts'

            # secret_key = os.getenv('secret_key')

            headers = self.__authentication_headers()

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

    # Corresponding endpoints to be tested
    def update_subaccount(self, id, business_name):
        url = f'https://api.flutterwave.com/v3/subaccounts/{id}'
        headers = self.__authentication_headers()
        payload = {
            "business_name": business_name
        }
        result = requests.put(url, json=payload,  headers=headers).json()
        return {'result': result}

        
    # Corresponding endpoints to be tested
    def fetch_settlement(self, id):
        url = f"https://api.flutterwave.com/v3/settlements/{id}"
        headers = self.__authentication_headers()

        subaccount = requests.get(url, headers=headers).json()

        return {'subaccount': subaccount}



class BadRequestToFlutterwave(APIException):
    status_code = 400
    default_detail = "Unable to create store, please ensure your account details are corrrect!!!"
    default_code = "error"