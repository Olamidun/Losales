from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.CreateItemAPIView.as_view(), name="create-item"),
    path('list',views.ListItemAPIView.as_view()),
    path('<int:pk>', views.RetrieveItemAPIView.as_view()),
    path('<int:pk>/edit', views.EditItemAPIView.as_view()),
    path('<int:pk>/add_images', views.CreateItemImageAPIView.as_view()),
    path('<int:pk>/images', views.ListImageAPIView.as_view()),
    # path('<int:pk>/image/<int:pk1>/', views.DeleteItemImageAPIView.as_view())
]