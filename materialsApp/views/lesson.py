from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import generics

from materialsApp.models import Lesson
from materialsApp.serializers import LessonSerializer
from usersApp.permissions import IsModer, IsOwner

"""Контроллер на основе genetic для создания"""


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

    def get_permissions(self):
        self.permission_classes = [~IsModer | IsAdminUser | IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


"""Контроллер на основе genetic для получения всех объектов"""


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsModer | IsAdminUser | IsOwner]
        return super().get_permissions()


"""Контроллер на основе genetic для получения одного объекта"""


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsModer | IsAdminUser | IsOwner]
        return super().get_permissions()


"""Контроллер на основе genetic для редактирования"""


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsModer | IsAdminUser | IsOwner]
        return super().get_permissions()


"""Контроллер на основе genetic для удаления"""


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ~IsModer | IsAdminUser | IsOwner]
        return super().get_permissions()
