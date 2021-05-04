from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('create_store', views.CreateStoreAPIView.as_view(), name="create-store"),
    path('edit_store/<str:slug>', views.UpdateStoreAPIView.as_view(), name="edit-store"),
    path('my_stores', views.ListStoresAPIView.as_view(), name="my-stores"),
    path('<str:slug>', views.StoreDetailsAPIView.as_view(), name="store-details"),
    
    path('<str:slug>/items/', include('items.urls'))
]