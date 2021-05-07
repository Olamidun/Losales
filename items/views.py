from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item
from stores.models import Store

# Create your views here.


class CreateItemAPIView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        return Item.objects.filter(store=store)
    def perform_create(self, serializer):
        store = Store.objects.get(slug=self.kwargs['slug'])
        serializer.save(store=store)

class EditItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        item = Item.objects.filter(store=store)
        return item
        
        