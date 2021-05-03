from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    twitter_handle = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    instagram_handle = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.email}'s Store"
