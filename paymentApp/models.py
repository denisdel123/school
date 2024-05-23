from django.db import models

from app import settings
from materialsApp.models import Course, Lesson

NULLABLE = {
    "null": True,
    "blank": True
}


class Payment(models.Model):
    amount = models.PositiveIntegerField(
        verbose_name='Сумма платежа',
        help_text='Введите сумму'
    )
    course = models.ForeignKey(
        Course,
        **NULLABLE,
        verbose_name='Курс',
        help_text='Укажите курс',
        on_delete=models.SET_NULL,
    )
    lesson = models.ForeignKey(
        Lesson,
        **NULLABLE,
        verbose_name='Урок',
        help_text='Укажите урок',
        on_delete=models.SET_NULL,
    )
    session_id = models.CharField(
        max_length=255,
        **NULLABLE,
        verbose_name='ID сессии',
        help_text='Укажите ID сессию',
    )
    link = models.URLField(
        max_length=400,
        **NULLABLE,
        verbose_name='Ссылка на оплату',
        help_text='Укажите ссылку на оплату',
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        **NULLABLE,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text='Укажите пользователя',
    )

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return self.amount
