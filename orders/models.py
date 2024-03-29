import string
import random
from django.db import models
from stores.models import Store
from items.models import Item

# Create your models here.


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    total_cost = models.DecimalField(decimal_places=3, max_digits=12, default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.TextField()
    reference = models.CharField(max_length=200)

    def assign_reference(self):
        rand = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(16)])
        self.reference = rand
        return self.save()


    def calculate_total_cost(self):
        order_items = OrderItem.objects.filter(order=self)
        # order_item_total = order_items.annotate(total_item_price=models.ExpressionWrapper(models.F('items__price') * models.F('quantity'), output_field=models.FloatField()))
        order_total = order_items.aggregate(order_total=models.Sum('total_cost'))

        self.total_cost = order_total['order_total']
        return self.save()
        
    

    def __str__(self):
        return f"{self.store.name}'s Order for {self.full_name}"



class OrderItem(models.Model):
    losales_commission = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    seller_commission = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_cost = models.DecimalField(decimal_places=3, max_digits=12, default=0)

    
class OrderPayment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reference = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference

