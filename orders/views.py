import requests
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .exceptions import InvalidOrderIdForStore, InvalidOrderItemIdForOrder
from .serializers import CreateOrderSerializer, OrderItemListSerializer, OrderSerializer, OrderPaymentSerializer
from .payment import pay_with_flutterwave, confirm_payment
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

class MakePayment(APIView):
    def get(self, request, pk, slug):
        store = Store.objects.get(slug=slug)
        print(store)
        
        order = Order.objects.select_related('store').get(pk=pk)
        print(order)
        if order.store == store:
            r = pay_with_flutterwave(order.total_cost, order.email, order.full_name, order.store.name, order.reference, store.subaccount_id, order.id)
            serializer = OrderPaymentSerializer(order)
            context = serializer.data
            if r['response']['status'] == "success":
                context['payment_info'] = r['response']
                return Response({'data': context})


class ConfirmPayment(APIView):
    def get(self, request, pk, slug):
        transaction_id = request.GET.get('transaction_id')
        store = Store.objects.get(slug=slug)
        print(store)
        
        order = Order.objects.select_related('store').get(pk=pk)
        print(order)
        if order.store == store:
            reference = order.reference
            r = confirm_payment(transaction_id)
            print(r)
            serializer = OrderPaymentSerializer(order)
            context = serializer.data
            if r['response']['data']['tx_ref'] == reference and r['response']['status'] == "success" and r['response']['data']['charged_amount'] == order.total_cost:
                order.paid = True
                order.save()
                context['payment_info'] = {'status': r['response']['status'], 'message': r['response']['message']}
                return Response({"data": context})




        