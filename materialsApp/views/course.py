from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from materialsApp.models import Course
from materialsApp.paginations import CustomPagination
from materialsApp.serializers import CourseSerializer
from usersApp.permissions import IsModer, IsOwner

"""Контроллер на основе ViewSet"""


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_permissions(self):

        if self.action == 'create':
            self.permission_classes = (IsAuthenticated, ~IsModer,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, ~IsModer | IsOwner,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsAuthenticated, IsModer | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        return super().perform_create(serializer)

    def get_queryset(self):
        if self.request.user.groups.filter(name='modern').exists():
            return Course.objects.all().order_by("name")
        else:
            return Course.objects.all().filter(owner=self.request.user).order_by("name")
