from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create_order', views.CreateOrderOnCheckoutAPIView.as_view()),
    path('orders', views.OrderAPIView.as_view()),
    path('<int:pk>', views.OrderDetailsAPIView.as_view()),
    path('<int:pk>/delete', views.DeleteOrderAPIView.as_view()),
    path('<int:pk>/order_items', views.ListOrderItemAPIView.as_view()),
    path('<int:pk>/order_items/<int:id>', views.OrderItemDetailAPIView.as_view()),
    path('<int:pk>/make_payment', views.MakePayment.as_view())
]