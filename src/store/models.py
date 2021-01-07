from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.

class Store(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    instagram_handle = models.CharField(max_length=100, null=True, blank=True)
    dispatch_rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='rider')
    reference = models.CharField(max_length=16, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    name_of_product = models.CharField(max_length=200)
    product_description = models.TextField()
    image = models.ImageField(upload_to="images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    # shipping = models.BooleanField(default=False)
    shipping_fee = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self):
        return f"{self.name_of_product} in {self.store.name}"

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

        print(url)

