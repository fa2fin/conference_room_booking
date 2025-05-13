from django.apps import AppConfig


class RoomsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rooms'

    def ready(self):
        # Опционально: можно подключить сигналы или выполнить инициализацию
        import rooms.signals  # Если используются сигналы (например, для аудита)