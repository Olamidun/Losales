from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.CreateItemAPIView.as_view(), name="create-item"),
    path('<int:pk>', views.EditItemAPIView.as_view())
]