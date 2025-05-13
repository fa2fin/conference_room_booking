from django.apps import AppConfig


class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'

    def ready(self):
        # Опционально: место для регистрации сигналов
        import bookings.signals  # Если используются сигналы