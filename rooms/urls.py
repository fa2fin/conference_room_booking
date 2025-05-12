from django.urls import path
from . import views

app_name = 'rooms'  # Уникальное пространство имён

urlpatterns = [
    path('', views.room_list, name='list'),
    path('create/', views.room_create, name='create'),  # Добавьте эту строку
    path('<int:pk>/', views.room_detail, name='detail'),
]