from django.db import models
from stores.models import Store
from items.models import Item

# Create your models here.


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    total_cost = models.DecimalField(decimal_places=3, max_digits=12, default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    

    def __str__(self):
        return f"{self.store.owner}'s Order for {self.full_name}"



class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_cost = models.DecimalField(decimal_places=3, max_digits=12, default=0)


    


class BillingAddress(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.name