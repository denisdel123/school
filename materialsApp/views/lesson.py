from rest_framework.viewsets import generics

from materialsApp.models import Lesson
from materialsApp.serializers import LessonSerializer

"""Контроллер на основе genetic для создания"""


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


"""Контроллер на основе genetic для получения всех объектов"""


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""Контроллер на основе genetic для получения одного объекта"""


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""Контроллер на основе genetic для редактирования"""


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""Контроллер на основе genetic для удаления"""


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
