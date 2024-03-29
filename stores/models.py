from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count

User = get_user_model()

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    store_image = models.ImageField(upload_to="store_image")
    twitter_handle = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    s_id = models.IntegerField(null=True, blank=True)
    subaccount_id = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    instagram_handle = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class ReviewStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    review = models.TextField()


    def __str__(self):
        return f"{self.store.name}'s review"

