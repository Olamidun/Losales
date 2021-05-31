from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .models import Store, ReviewStore
from .serializers import CreateStoreSerializer, ListStoreSerializer, ReviewStoreSerializer

# Create your views here.

class CreateStoreAPIView(generics.CreateAPIView):
    serializer_class = CreateStoreSerializer
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpdateStoreAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CreateStoreSerializer
    lookup_field = "slug"
    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user) 


class ListStoresAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ListStoreSerializer
    def get_queryset(self):
        print(self.kwargs)
        stores = Store.objects.filter(owner=self.request.user)
        return stores

class StoreDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = ListStoreSerializer
    lookup_field = "slug"

    def get_queryset(self):
        store = Store.objects.filter(slug=self.kwargs.get('slug'))
        print(store)
        return store


'''

Store Review endpoints

'''

class CreateStoreReviewAPI(generics.ListCreateAPIView):
    serializer_class = ReviewStoreSerializer

    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        return ReviewStore.objects.filter(store=store)
    def perform_create(self, serializer):
        store = Store.objects.get(slug=self.kwargs['slug'])
        serializer.save(store=store)
