from rest_framework import viewsets

from usersApp.models import User
from usersApp.serializers import UserSerializers

"""Контроллер ViewSet для модели User"""


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
