from django.contrib import admin
from .models import Order, OrderItem, OrderPayment

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_cost', 'paid', 'time_created', 'store']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['items', 'quantity', 'order', 'seller_commission',  'losales_commission'] 


class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'reference', 'timestamp'] 

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(OrderPayment, OrderPaymentAdmin)