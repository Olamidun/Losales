from django.contrib import admin
from .models import Order, OrderItem, OrderPayment

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['store', 'total_cost', 'paid', 'time_created']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['items', 'quantity', 'order'] 


class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'reference', 'timestamp'] 

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(OrderPayment, OrderPaymentAdmin)