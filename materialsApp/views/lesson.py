from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import generics

from materialsApp.models import Lesson
from materialsApp.paginations import CustomPagination
from materialsApp.serializers import LessonSerializer
from usersApp.permissions import IsModer, IsOwner

"""Контроллер на основе genetic для создания"""


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'materialsApp/lesson_create.html'

    def get_permissions(self):
        # self.permission_classes = [~IsModer | IsAdminUser | IsOwner]
        self.permission_classes = [AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

    def get(self, request, *args, **kwargs):
        serializer = LessonSerializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = LessonSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('materialsApp:lesson_list')


"""Контроллер на основе genetic для получения всех объектов"""


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = CustomPagination

    # renderer_classes = [JSONRenderer]
    # template_name = 'materialsApp/lesson_list.html'

    def get_permissions(self):
        permissions = []
        if self.request.user.groups.filter(name='modern').exists():
            permissions = [IsAuthenticated, IsModer | IsAdminUser | IsOwner]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

    # def get(self, request, *args, **kwargs):
    #    queryset = self.get_queryset()
    #    serializer = self.serializer_class(queryset, many=True)
    #    return Response(serializer.data)

    def get_queryset(self):
        if self.request.user.groups.filter(name='modern').exists():
            return Lesson.objects.all().order_by('name')
        else:
            return Lesson.objects.filter(owner=self.request.user).order_by('name')


"""Контроллер на основе genetic для получения одного объекта"""


class LessonRetrieveAPIView(generics.RetrieveAPIView):

    def get_serializer_class(self):
        return LessonSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsModer | IsAdminUser | IsOwner]
        return super().get_permissions()

    def get_queryset(self):
        return Lesson.objects.all().order_by('name')


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
