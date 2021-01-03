from django.db import models
from django.conf import settings

# Create your models here.

class Store(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    dispatch_rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='rider')
    reference = models.CharField(max_length=16, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner.first_name} {self.owner.last_name}'s Store"

    
    def save(self, *args, **kwargs):
        if self.url == '':
            self.url = f'http://localhost:8000/store/{self.owner.first_name}-{self.owner.last_name}'
        super(Store, self).save(*args, **kwargs)


class Product(models.Model):
    name_of_product = models.CharField(max_length=200)
    product_description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_of_product} in {self.store.owner.first_name} {self.store.owner.last_name}'s Store"

