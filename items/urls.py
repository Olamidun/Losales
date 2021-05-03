from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('<int:pk>/create_item', views.CreateItemAPIView.as_view(), name="create-item"),
]