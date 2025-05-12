from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # Кастомизация админ-панели для залов
    list_display = ('name', 'capacity', 'has_projector', 'is_active')
    list_filter = ('is_active', 'has_projector')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'capacity')
        }),
        ('Оборудование', {
            'fields': ('has_projector', 'has_whiteboard')
        }),
        ('Статус', {
            'fields': ('is_active',)
        })
    )