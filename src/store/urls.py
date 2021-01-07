from django.urls import path
from . import views

app_name= "store"

# STORE URL PATHS
urlpatterns = [
    path('<str:slug>/dashboard', views.dashboard_view, name="dashboard"),
    path('<str:slug>', views.store, name="store"),
    path('create_store', views.create_store, name="create-store"),
    path('<str:slug>/pay_for_store', views.pay_for_store, name="pay-for-store"),
    path('<str:slug>/add_product', views.add_product_to_store, name="add_product"),
    path('edit_product/<int:pk>', views.edit_product, name="edit_product"),
    path('confirm_payment/<str:slug>', views.confirm_payment, name="confirm-payment")
]