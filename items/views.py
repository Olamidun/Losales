from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item
from stores.models import Store

# Create your views here.


class CreateItemAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )

    # def get_queryset(self):
        # print('your kwargs', self.kwargs)
        # store = Store.objects.get(id=self.kwargs['store'])
        # return Item.objects.filter(store=store)
    def perform_create(self, serializer):
        print(self.kwargs)
        store = Store.objects.get(id=self.kwargs.get('pk'))
        print(store)
        serializer.save(store=store)