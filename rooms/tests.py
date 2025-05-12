from django.test import TestCase, Client
from django.urls import reverse
from .models import Room
from users.models import CustomUser
class RoomTests(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.room = Room.objects.create(
            name="Test Hall",
            capacity=15,
            has_projector=True
        )
        self.client = Client()

    def test_room_creation(self):
        # Проверка создания объекта Room
        self.assertEqual(self.room.capacity, 15)
        self.assertTrue(self.room.has_projector)

    def test_room_list_view(self):
        # Проверка доступности списка залов
        response = self.client.get(reverse('rooms:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Hall")

    def test_room_detail_view(self):
        # Проверка детальной страницы зала
        url = reverse('rooms:detail', args=[self.room.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "capacity: 15")

    def test_admin_room_creation(self):
        # Проверка доступа к админке
        admin_user = CustomUser.objects.create_superuser(
            email='admin@test.com',
            password='adminpass'
        )
        self.client.login(email='admin@test.com', password='adminpass')
        response = self.client.get('/admin/rooms/room/')
        self.assertEqual(response.status_code, 200)