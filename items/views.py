from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .serializers import ItemSerializer, ListItemSerializer
from .models import Item
from stores.models import Store

# Create your views here.


class CreateItemAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )

    # def get_queryset(self):
    #     store = Store.objects.get(slug=self.kwargs['slug'])
    #     return Item.objects.filter(store=store)
    def perform_create(self, serializer):
        store = Store.objects.get(slug=self.kwargs['slug'])
        serializer.save(store=store)


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
        item = Item.objects.filter(store=store, pk=self.kwargs.get('pk'))
        return item

class DeleItemAPIView(generics.DestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        item = Item.objects.filter(store=store, pk=self.kwargs.get('pk'))
        return item


# class CreateItemImageAPIView(generics.CreateAPIView):
#     permission_classes= (IsAuthenticated, )
#     serializer_class = ItemImageSerializer

#     def perform_create(self, serializer):
#         item = Item.objects.get(pk=self.kwargs['pk'])
#         serializer.save(item=item)


# class ListImageAPIView(generics.ListAPIView):
#     serializer_class = ItemImageSerializer

#     def get_queryset(self):
#         item = Item.objects.get(pk=self.kwargs['pk'])
#         item_images = ItemImage.objects.filter(item=item)
#         return item_images

'''
Hasn't been properly done
'''
# class DeleteItemImageAPIView(generics.RetrieveDestroyAPIView):
#     permission_classes = (IsAuthenticated, )
#     serializer_class = ItemImageSerializer


#     def get_queryset(self):
#         item = Item.objects.get(pk=self.kwargs['pk'])
#         image = ItemImage.objects.filter(item=item)
#         return image