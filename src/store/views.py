import random
import string
import requests
from django.shortcuts import redirect, render, HttpResponse
from .forms import StoreForm, ProductForm
from accounts.models import Account
from .models import Store, Product
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.



public_key = 'FLWPUBK_TEST-aaab004122d871bc5c7ea7ade0048fd9-X'

secret_key = 'FLWSECK_TEST-6780cf75dc1d85b632abee0f01420b9a-X'

@login_required
def dashboard_view(request, first_name, last_name):
    user = Account.objects.get(first_name=first_name, last_name=last_name)
    
    store = Store.objects.get(owner=user) #This is going to be r
    stores = Store.objects.filter(owner=request.user)
    products = Product.objects.filter(store=store).all()
    number_of_stores = stores.count()
    return render(request, 'store/dashboard.html', {'store': store, 'products': products, "number_of_stores": number_of_stores})

@login_required
def create_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            country = form.cleaned_data['country']
            store = Store.objects.create(owner=request.user, name=name, description=description, country=country)
        return redirect('store:pay-for-store')
    else:
        form = StoreForm()
    return render(request, 'store/create_store.html', {'form': form})


@login_required
def pay_for_store(request):
    base_url = 'https://api.flutterwave.com/v3/payments'

    store = Store.objects.get(owner=request.user, is_approved=False)
    print(store)
    rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])

    tx_ref = rand

    headers = {'Authorization': f"Bearer {secret_key}"}

    payload = {
        "tx_ref": tx_ref,
        "amount": "100",
        "currency": "NGN",
        "redirect_url": "http://localhost.com/store/dashboard",
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

    response = requests.post(base_url, json=payload, headers=headers)
    results = response.json()

    redirect_link = results['data']['link']
    return redirect(redirect_link)

@login_required
def confirm_payment(request):
    # https://www.google.com/?status=successful&tx_ref=hhyDkx2FnGTZJOo5&transaction_id=1809806
    # http://localhost.com/store/dashboard?status=successful&tx_ref=uWgg6zkUWTnXx3JW&transaction_id=1809860

    # transaction_id = request.GET.get('transaction_id')


    # headers = {"Content-Type": 'application/json', 'Authorization': f"Bearer {secret_key}"}

    # base_url = f'https://api.flutterwave.com/v3/transactions/{headers}/verify'

    # response = requests.get(base_url, headers)
    # results = response.json()
    # print(transaction_id)
    # return HttpResponse(results)
    pass

@login_required
def add_product_to_store(request, name):
    try:
        store = Store.objects.get(name=name, owner=request.user)
    except Store.DoesNotExist:
        return HttpResponse('Store not found')
    if store.is_approved == True:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name_of_product']
                price = form.cleaned_data['price']
                description = form.cleaned_data['product_description']
                product = Product.objects.create(name_of_product=name, price=price, product_description=description, store=store)
            return redirect('store:dashboard', first_name=request.user.first_name, last_name=request.user.last_name)
        else:
            form = ProductForm()
    else:
        return HttpResponse('Your store is not approved yet so you cannot add products')
    return render(request, 'store/add_product.html', {'form': form})


@login_required
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.user == product.store.owner:
        if request.method == 'POST':
            form = ProductForm(request.POST or None, instance=product)
            if form.is_valid():
                form.save()
            return redirect('store:dashboard', first_name=request.user.first_name, last_name=request.user.last_name)
        else:
            form = ProductForm(instance=product)
    else:
        return HttpResponse('You were not the one that added this product, that means you cannot edit it')
    return render(request, "store/edit_product.html", {'form': form})

# def delete_product(request, pk):
    # try:
    #     product = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     return HttpResponse('The product you want to delete cannot be found')
    # if request.method == "DELETE":
    #     product.delete()
    #     return redirect('store:dashboard', first_name=request.user.first_name, last_name=request.user.last_name)
    pass
    
