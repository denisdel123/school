from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

"""Модель пользователя"""


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(**NULLABLE, verbose_name='Аватар')
    phone = models.CharField(max_length=40, **NULLABLE, verbose_name='Телефон')
    city = models.CharField(max_length=30, **NULLABLE, verbose_name='Город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
