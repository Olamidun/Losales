from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create_order', views.CreateOrderOnCheckoutAPIView.as_view()),
    path('<int:pk>/create_orderitem/', views.CreateOrderItemAPIView.as_view())
]