# Форма бронирования
from django import forms
from django.core.exceptions import ValidationError

from rooms.models import Room
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time', 'end_time', 'participants']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        participants = cleaned_data.get('participants')
        room_id = self.initial.get('room_id')

        # Валидация времени
        if start_time and end_time:
            if start_time >= end_time:
                raise ValidationError("Время окончания должно быть позже начала.")
            if start_time.date() != end_time.date():
                raise ValidationError("Бронирование возможно только в пределах одного дня.")

        # Валидация участников
        room = Room.objects.get(id=room_id)
        if participants and participants > room.capacity:
            raise ValidationError(f"Максимальная вместимость комнаты: {room.capacity} человек.")

        return cleaned_data

# bookings/apps.py
from django.apps import AppConfig

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'

    def ready(self):
        # Импорт сигналов
        import bookings.signals