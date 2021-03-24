import random
import string
import requests
from django.shortcuts import redirect, render, HttpResponse
from .forms import StoreForm, ProductForm
from accounts.models import Account
from .models import Store, Product
from cart.models import Order
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .functions import pay

# Create your views here.

