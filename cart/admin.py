from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'complete', 'date_ordered', 'transaction_id']
    list_display_links = ['transaction_id', 'customer']
    search_fields = ['customer__email', 'transaction_id']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'date_added']


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order', 'address', 'city', 'state', 'country', 'date_added']
    list_display_links = ['address', 'order']
    search_fields = ['customer__email']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
