from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from users.models import CustomUser
from rooms.models import Room
from .models import Booking

class BookingTests(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.room = Room.objects.create(
            name="Test Room",
            capacity=10,
            has_projector=True
        )
        self.booking = Booking.objects.create(
            user=self.user,
            room=self.room,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=2),
            participants=5
        )

    def test_booking_creation(self):
        # Проверка создания бронирования
        self.assertEqual(self.booking.status, 'pending')
        self.assertEqual(self.booking.room.name, "Test Room")

    def test_booking_conflict(self):
        # Проверка обнаружения конфликта времени
        conflicting_booking = Booking(
            user=self.user,
            room=self.room,
            start_time=timezone.now() + timezone.timedelta(minutes=30),
            end_time=timezone.now() + timezone.timedelta(hours=3),
            participants=3
        )
        self.assertTrue(conflicting_booking.is_conflict())

    def test_booking_list_view(self):
        # Тест доступа к списку бронирований
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('bookings:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Room")