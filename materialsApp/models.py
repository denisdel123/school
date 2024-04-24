from django.db import models

from usersApp.models import NULLABLE

"""Модель курса"""


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(**NULLABLE, upload_to='course/', verbose_name='Картинка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


"""Модель урока"""


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(**NULLABLE, upload_to='lesson/', verbose_name='Картинка')
    url_to_video = models.URLField(**NULLABLE, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='Курс', )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
