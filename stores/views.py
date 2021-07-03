import json
from django.http import request
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from .models import Store, ReviewStore
from .serializers import CreateStoreSerializer, ListStoreSerializer, ReviewStoreSerializer
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

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


# To be cached
class ListStoresAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ListStoreSerializer
    def get_queryset(self):
        print(cache)
        # print(self.kwargs)
        stores = cache.get('store')
        if stores is None:
            stores = Store.objects.filter(owner=self.request.user)
            cache.set('store', stores, 30)
            return stores
        #     print(stores)
        #     return stores
        else:
            return stores
            
        return stores


# To be cached
class StoreDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = ListStoreSerializer
    lookup_field = "slug"

    def get_queryset(self):
        store = cache.get('store_detail')
        print(store)
        if store is None:
            store = Store.objects.filter(slug=self.kwargs.get('slug'))
            cache.set('store_detail', store, 300)
            return store
        else:
            # cache.set('store_detail', json.dumps(store), 30)
            print(store)
            return store


'''
Store Review endpoints
'''

class CreateStoreReviewAPI(generics.ListCreateAPIView):
    serializer_class = ReviewStoreSerializer

    # To be cached
    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs['slug'])
        return ReviewStore.objects.filter(store=store)
    def perform_create(self, serializer):
        store = Store.objects.get(slug=self.kwargs['slug'])
        serializer.save(store=store)
        

class RetrieveReviewAPI(generics.RetrieveAPIView):
    serializer_class = ReviewStoreSerializer

    # To be cached
    def get_queryset(self):
        store = Store.objects.get(slug=self.kwargs.get('slug'))
        return ReviewStore.objects.filter(store=store, pk=self.kwargs.get('pk'))


