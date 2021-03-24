from django.db import models
from store.models import Product, Store
from django.conf import settings
from accounts.models import Customer

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    transaction_id = models.CharField(max_length=16, null=False)

    def __str__(self):
        return f'{self.customer.user.first_name} order'


    @property
    def get_order_total(self):
        order_items = self.orderitem_set.all()   
        total = sum([item.get_total for item in order_items])
        return total

    
    @property
    def get_order_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity  for item in order_items])
        return total


    @property
    def check_if_order_is_complete(self):
        if self.complete == False:
            return False
        return True

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name_of_product or ''

    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=16, null=False)
    city = models.CharField(max_length=16, null=False)
    state = models.CharField(max_length=16, null=False)
    country = models.CharField(max_length=16, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    is_billing_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address