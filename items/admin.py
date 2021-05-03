from django.contrib import admin
from .models import Item, ItemImage

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'store', 'discounted_price']


class ItemImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'item'] 

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
