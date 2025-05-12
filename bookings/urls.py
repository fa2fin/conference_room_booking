from django.urls import path
from .views import (
    create_booking,
    booking_list,
    booking_detail,
    cancel_booking
)

app_name = 'bookings'
urlpatterns = [
    # Создание бронирования
    path('create/<int:room_id>/', create_booking, name='create'),

    # Список бронирований пользователя
    path('my-bookings/', booking_list, name='list'),

    # Детали конкретного бронирования
    path('<int:pk>/', booking_detail, name='detail'),

    # Отмена бронирования
    path('<int:pk>/cancel/', cancel_booking, name='cancel'),
]