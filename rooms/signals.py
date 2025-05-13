from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Room
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Room)
def log_room_change(sender, instance, created, **kwargs):

    action = 'created' if created else 'updated'
    logger.info(f"Room {instance.name} was {action}")