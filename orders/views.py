from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .exceptions import InvalidOrderIdForStore, InvalidOrderItemIdForOrder
from .serializers import CreateOrderSerializer, OrderItemListSerializer, OrderSerializer
from .models import Order, OrderItem
from stores.models import Store
from items.models import Item


# Create your views here.


class CreateOrderOnCheckoutAPIView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer

    def get_queryset(self):
        return Item.objects.all()

    def perform_create(self, serializer):
        store = Store.objects.get(slug=self.kwargs['slug'])
        serializer.save(store=store)


# To be cached
class OrderAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        order = Order.objects.all().filter(store=store)
        return order

class OrderDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        order = Order.objects.filter(store=store, pk=self.kwargs['pk'])
        return order

class OrderDetailsAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        order = Order.objects.filter(store=store, pk=self.kwargs['pk'])
        return order

class DeleteOrderAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        order = Order.objects.filter(store=store, pk=self.kwargs['pk'])
        return order



class ListOrderItemAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderItemListSerializer

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        order = Order.objects.get(pk=self.kwargs['pk'])
        order_item = OrderItem.objects.filter(order=order)
        if order.store == store:
            return order_item
        else:
            raise InvalidOrderIdForStore()


class OrderItemDetailAPIView(generics.RetrieveAPIView):
    serializer_class = OrderItemListSerializer
    permission_classes = (IsAuthenticated, )

    lookup_field = "id"

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs.get('slug'))
        order = Order.objects.get(pk=self.kwargs.get('pk'))
        if order.store == store:
            
            order_item = OrderItem.objects.filter(order=order, id=self.kwargs.get('id'))
            print(order_item)
            for items in order_item:
                if order == items.order:
                    return order_item
                else:
                    raise InvalidOrderItemIdForOrder()
        else:
            raise InvalidOrderIdForStore()


        