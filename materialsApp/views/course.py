from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from materialsApp.models import Course
from materialsApp.paginations import CustomPagination
from materialsApp.serializers import CourseSerializer
from materialsApp.tasks import send_update
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

    def perform_update(self, serializer):
        instance = serializer.save()
        update_fields = {field: serializer.validated_data[field] for field in serializer.validated_data}
        send_update.delay(instance.id, update_fields)
        # print(instance.id)
        # print(update_fields)
        super().perform_update(serializer)

