from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('create_store', views.CreateStoreAPIView.as_view(), name="create-store"),
    path('edit_store/<str:slug>', views.UpdateStoreAPIView.as_view(), name="edit-store"),
    path('store/<int:pk>', views.StoreDetailsAPIView.as_view(), name="store-details"),
    path('my_stores', views.ListStoresAPIView.as_view(), name="my-stores")
]