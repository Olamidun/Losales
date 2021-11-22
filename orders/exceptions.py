from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


class InvalidOrderIdForStore(APIException):
    status_code = 404
    default_detail = "The order for this store cannot be found, please check order id again"
    default_code = "error"


class InvalidOrderItemIdForOrder(APIException):
    status_code = 404
    default_detail = "The order items for this order cannot be found, please check order item id again"
    default_code = "error"


class InvalidStoreOwner(APIException):
    status_code = 401
    default_detail = "You cannot perform this action for this store because you are not the owner of the store"
    default_code = "error"
    

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first, 
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    return response