from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name', 'item_image', 'price', 'store', 'discounted_price', 'out_of_stock']

admin.site.register(Item, ItemAdmin)

