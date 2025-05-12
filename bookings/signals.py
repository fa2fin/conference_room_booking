# bookings/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Booking

@receiver(post_save, sender=Booking)
def handle_booking_status(sender, instance, created, **kwargs):
    """Пример обработчика сигналов для бронирований"""
    if created:
        print(f"New booking created: {instance}")
    else:
        print(f"Booking updated: {instance}")