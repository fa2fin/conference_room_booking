# Главные URL-маршруты
from django.contrib import admin
from django.urls import path, include
# conference_room_booking/urls.py
#path('api/check_availability/', include('bookings.api.urls')),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('rooms/', include('rooms.urls')),
    path('bookings/', include('bookings.urls')),
    path('', include('rooms.urls')),
]