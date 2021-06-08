from django.contrib import admin
from .models import Order, OrderItem, BillingAddress

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['store', 'total_cost', 'paid', 'time_created']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['items', 'quantity', 'order'] 


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'order' ,'address'] 

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)