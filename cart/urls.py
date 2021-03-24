from django.urls import path
from . import views

app_name= "cart"

urlpatterns = [
    path('', views.cart, name="cart"),
    path('update_item', views.update_item, name='update-item'),
    path('checkout', views.checkout, name="checkout"),
    path('process_order', views.process_order, name="process_order")
]