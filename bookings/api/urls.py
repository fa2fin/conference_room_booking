from django.urls import path
from . import views

app_name = 'bookings_api'

urlpatterns = [
    # Пока оставьте пустым или добавьте временный маршрут
    path('check/', views.check_availability, name='check'),
]