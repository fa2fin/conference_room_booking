from django.urls import path
from .views import (
    create_booking,
    booking_list,
    booking_detail,
    cancel_booking
)

app_name = 'bookings'  # Пространство имен для URL

urlpatterns = [
    # Создание бронирования (URL: /bookings/create/<room_id>/)
    path('create/<int:room_id>/', create_booking, name='create'),

    # Список бронирований пользователя (URL: /bookings/my-bookings/)
    path('my-bookings/', booking_list, name='list'),

    # Детали бронирования (URL: /bookings/<pk>/)
    path('<int:pk>/', booking_detail, name='detail'),

    # Отмена бронирования (URL: /bookings/<pk>/cancel/)
    path('<int:pk>/cancel/', cancel_booking, name='cancel'),
]