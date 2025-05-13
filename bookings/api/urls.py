from django.urls import path
from . import views

app_name = 'bookings_api'

urlpatterns = [
    path('check/', views.check_availability, name='check'),
]