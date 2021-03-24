from django.contrib import admin
from .models import Store, Product

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'country', 'slug', 'dispatch_rider', 'is_approved']
    # list_display_links = ['user', 'billing_address', 'payment']
    search_fields = ['owner__email', 'reference']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['store', 'name_of_product', 'price']


admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)