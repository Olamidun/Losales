from django.db import models
from stores.models import Store
from cloudinary.models import CloudinaryField
# from

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store')
    item_image = models.ImageField(upload_to="item_image")
    discounted_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    out_of_stock = models.BooleanField(default=False)
    def __str__(self):
        return self.name


# class ItemImage(models.Model):
#     image = models.ImageField()
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.item.name} image'