from rest_framework import serializers

from usersApp.models import User

"""Сериализатор для контроллера UserViewSet"""


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
