from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .serializers import ItemSerializer, ListItemSerializer
from .models import Item
from stores.models import Store
from orders.exceptions import InvalidStoreOwner

# Create your views here.


class CreateItemAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        store = Store.objects.get(slug=self.kwargs['slug'])
        if store.owner == self.request.user:
            serializer.save(store=store)
        
        else:
            raise InvalidStoreOwner()


class ListItemAPIView(generics.ListAPIView):
    serializer_class = ListItemSerializer

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        return Item.objects.filter(store=store)


class RetrieveItemAPIView(generics.RetrieveAPIView):
    serializer_class = ListItemSerializer
    lookup_field = "pk"

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        return Item.objects.filter(store=store, pk=self.kwargs.get('pk'))

class EditItemAPIView(generics.UpdateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        if store.owner == self.request.user:
            item = Item.objects.filter(store=store, pk=self.kwargs.get('pk'))
            return item
        else:
            raise InvalidStoreOwner()

class DeleItemAPIView(generics.DestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        if store.owner == self.request.user:

            item = Item.objects.filter(store=store, pk=self.kwargs.get('pk'))
            return item
        else: 
            raise InvalidStoreOwner()
