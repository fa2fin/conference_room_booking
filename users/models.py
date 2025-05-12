# Модель пользователя
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None  # Отключаем стандартное поле
    email = models.EmailField(unique=True)
    ROLES = (
        ('user', 'Regular User'),
        ('admin', 'Administrator'),
    )

    # Добавляем поле role
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='user',
        verbose_name='Роль'
    )

    USERNAME_FIELD = 'email'  # Используем email для входа
    REQUIRED_FIELDS = []  # Убираем username из обязательных полей

    objects = CustomUserManager()  # Подключаем кастомный менеджер
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
