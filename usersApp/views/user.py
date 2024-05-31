from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from usersApp.models import User
from usersApp.permissions import IsOwner
from usersApp.serializers import UserOwnerSerializers, UserSerializers, UserListSerializers

"""Контроллер ViewSet для модели User"""


@receiver(user_logged_in)
def handle_user_login(sender, user, request, **kwargs):
    user.profile.last_login = timezone.now()
    user.profile.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action == 'update':
            self.permission_classes = (IsAuthenticated, IsOwner,)
        elif self.action == 'retriever':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, IsOwner,)

        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializers
        elif self.action == 'retriever' or self.request.user == self.get_object():
            return UserOwnerSerializers
        else:
            return UserSerializers
