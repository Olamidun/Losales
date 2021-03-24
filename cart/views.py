import random
import string
import json
import requests
from django.shortcuts import render, redirect
from store.models import Store, Product
from .models import Order, OrderItem, ShippingAddress
from django.http import JsonResponse
from .utils import cookie_cart, cart_data
from accounts.models import Customer

# Create your views here.






    
