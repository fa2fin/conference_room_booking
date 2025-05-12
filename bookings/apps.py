from django.apps import AppConfig


class BookingsConfig(AppConfig):
    # Базовая конфигурация приложения бронирований
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'  # Имя приложения

    def ready(self):
        # Опционально: место для регистрации сигналов
        import bookings.signals  # Если используются сигналы