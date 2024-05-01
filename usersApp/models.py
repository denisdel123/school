from django.contrib.auth.models import AbstractUser
from django.db import models

from app import settings
from materialsApp.models import Course, Lesson

NULLABLE = {
    'null': True,
    'blank': True
}

PAYMENT_METHOD = (
    ('cash', 'Наличные'),
    ('transfer', 'Перевод на счет'),

)

"""Модель пользователя"""


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(**NULLABLE, verbose_name='Аватар')
    phone = models.CharField(max_length=40, **NULLABLE, verbose_name='Телефон')
    city = models.CharField(max_length=30, **NULLABLE, verbose_name='Город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.CASCADE, related_name='user_p')
    at_payment = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, related_name='Оплаченный_курс')
    paid_lesson = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.CASCADE, related_name='Оплаченный_урок')
    sum_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    method_paid = models.CharField(max_length=30, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('at_payment',)

