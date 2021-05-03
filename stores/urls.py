from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('create_store', views.CreateStoreAPIView.as_view(), name="create-store"),
    path('edit_store/<int:pk>', views.UpdateStoreAPIView.as_view(), name="edit-store"),
    path('my_stores', views.ListStoresAPIView.as_view(), name="my-stores")
]