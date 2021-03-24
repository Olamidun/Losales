from django.urls import path
from . import views

app_name= "store"

# STORE URL PATHS
urlpatterns = [
    path('', views.home, name="home"),
    path('store_list', views.store_list, name="store-list"),
    path('<str:slug>/dashboard', views.dashboard_view, name="dashboard"),
    path('create_store/', views.create_store, name="create-store"),
    path('<str:slug>', views.store, name="store"),
    
    path('<str:slug>/pay_for_store', views.pay_for_store, name="pay-for-store"),
    path('<str:slug>/add_product', views.add_product_to_store, name="add_product"),
    path('edit_product/<int:pk>', views.edit_product, name="edit_product"),
    path('confirm_payment/<str:slug>', views.confirm_payment, name="confirm-payment"),
    path('<str:slug>/pay-for-store', views.payment_page, name="payment"), 
    path('create_subaccount/<str:slug>', views.create_subaccount, name="subaccount")
]