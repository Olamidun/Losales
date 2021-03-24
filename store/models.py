import uuid
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.

class Store(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=200)
    bank_code = models.IntegerField(null=True)
    account_number = models.IntegerField(null=True)
    slug = models.SlugField(null=False, unique=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    instagram_handle = models.CharField(max_length=100, null=True, blank=True)
    store_subaccount_id = models.CharField(max_length=200, blank=True, null=True)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_of_product = models.CharField(max_length=200)
    product_description = models.TextField()
    image = models.ImageField(upload_to="images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
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













from django.db import models
from django.conf import settings

# Create your models here.


class CableTv(models.Model):
    DSTV = 'DSTV'
    GOTV = 'GOTV'
    STARTIMES = 'STAR'

    CABLE_TV_SERVICES = (
        (DSTV, 'dstv'),
        (GOTV, 'gotv'),
        (STARTIMES, 'star')
    )

    CABLE_TV_PLANS = [
    ('Gotv', (
            ('max', 'GOTV Max'),
            ('jolli', 'GOTV Jolli'),
            ('jinja', 'GOTV Jinja'),
            ('gosmann', 'GOTV SMALLIE Annually'),
            ('gosmalmon', 'GOTV SMALLIE Monthly'),
            ('gosmalQua', 'GOTV SMALLIE Quartely'),
        )
    ),

    ('DSTV', (
            ('premium', 'DSTV Premium'),
            ('compactplus', 'DSTV Compact Plus'),
            ('compact', 'DSTV Compact'),
            ('confam', 'DSTV Confam'),
            ('Yanga', 'DSTV Yanga'),
            ('padi', 'DSTV Padi'),
        )
    ),

    # ('STAR', (
    #         ('premium', 'DSTV Premium'),
    #         ('compactplus', 'DSTV Compact Plus'),
    #         ('compact', 'DSTV Compact'),
    #         ('confam', 'DSTV Confam'),
    #         ('Yanga', 'DSTV Yanga'),
    #         ('padi', 'DSTV Padi'),
    #     )
    # ),
    ('unknown', 'Unknown'),
    ]


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cable_tv = models.CharField(max_length=10, choices=CABLE_TV_SERVICES, default=DSTV)
    plan = models.CharField(max_length=30, choices=CABLE_TV_PLANS)
    # price = models.DecimalField(decimal_places=5, max_digits=10, null=True, blank=True)
    smart_card_number = models.BigIntegerField()
    code = models.CharField(max_length=10)
    request_id = models.CharField(max_length=100)
    

