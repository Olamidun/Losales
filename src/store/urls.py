from django.urls import path
from . import views

app_name= "store"

# STORE URL PATHS
urlpatterns = [
    path('<str:first_name>-<str:last_name>/dashboard', views.dashboard_view, name="dashboard"),
    path('create_store', views.create_store, name="create-store"),
    path('pay_for_store', views.pay_for_store, name="pay-for-store"),
    path('<str:name>/add_product', views.add_product_to_store, name="add_product"),
    path('edit_product/<int:pk>', views.edit_product, name="edit_product"),
    # path('dashboard', views.confirm_payment, name="confirm-payment")
]