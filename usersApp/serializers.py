from rest_framework import serializers

from usersApp.models import User, Payments

"""Сериализатор для контроллера UserViewSet"""


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
