from rest_framework import generics, serializers
from .serializers import CreateOrderSerializer, CreateOrderItemSerializer
from .models import Order, OrderItem
from stores.models import Store
from items.models import Item

# Create your views here.


class CreateOrderOnCheckoutAPIView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer

    # def get_queryset(self):
    #     return Item.objects.all()

    def perform_create(self, serializer):
        store = Store.objects.get(slug=self.kwargs['slug'])
        serializer.save(store=store)


class CreateOrderItemAPIView(generics.CreateAPIView):
    serializer_class = CreateOrderItemSerializer

    def perform_create(self, serializer):
        order = Order.objects.get(id=self.kwargs['pk'])
        serializer.save(order=order)